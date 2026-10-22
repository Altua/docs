"""Render the current Markdown master without rewriting its content."""
from pathlib import Path
import html
import re
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, KeepTogether, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]

def build(illustrated=False, source_name=None, label=None):
    from customer_guide_graphics import Explanation, INSERTIONS
    for name, filename in [('Guide', 'arial.ttf'), ('GuideBold', 'arialbd.ttf')]:
        pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/' + filename))
    pdfmetrics.registerFontFamily('Guide', normal='Guide', bold='GuideBold',
        italic='Guide', boldItalic='GuideBold')
    ink, teal = colors.HexColor('#182330'), colors.HexColor('#126B70')
    base = dict(fontName='Guide', fontSize=10, leading=14, textColor=ink, spaceAfter=8)
    styles = {'p': ParagraphStyle('p', **base)}
    for level, size in [(1, 24), (2, 16), (3, 12)]:
        styles[str(level)] = ParagraphStyle(str(level), fontName='GuideBold',
            fontSize=size, leading=size+5, textColor=teal, spaceBefore=14,
            spaceAfter=9, keepWithNext=True)
    styles['cell'] = ParagraphStyle('cell', **{**base, 'fontSize':9, 'leading':12, 'spaceAfter':0})
    styles['note'] = ParagraphStyle('note', **{**base, 'fontSize':9, 'leading':12},
        backColor=colors.HexColor('#EEF5F4'), borderPadding=8, spaceBefore=8)

    def inline(text):
        text = html.escape(text)
        text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)',
            r'<link href="\2" color="#126B70"><u>\1</u></link>', text)
        text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
        text = re.sub(r'`([^`]+)`', r'<font color="#126B70">\1</font>', text)
        return text

    def p(text, style='p'):
        return Paragraph(inline(text), styles[style])

    source = ROOT/'drafts'/(source_name or 'grunt-one-customer-guide.md')
    lines = source.read_text(encoding='utf-8-sig').splitlines()
    story, i = [], 0
    width = A4[0]-88
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line == '<!-- pagebreak -->':
            story.append(PageBreak())
            i += 1
            continue
        if line.startswith('<!-- graphic:'):
            story.append(Explanation(line.split(':',1)[1].split('-->')[0].strip()))
            i += 1
            continue
        if line.startswith('|'):
            rows = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            n = len(rows[0])
            ratios = [0.22, 0.39, 0.39] if n == 3 else [0.32, 0.68]
            table = Table([[p(('**'+c+'**') if r == 0 and c else c, 'cell')
                for c in row] for r, row in enumerate(rows)],
                colWidths=[width*x for x in ratios], repeatRows=1, hAlign='LEFT')
            table.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,0),colors.HexColor('#DEEDEB')),
                ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#F5F7F8')]),
                ('VALIGN',(0,0),(-1,-1),'TOP'),
                ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
                ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
                ('LINEBELOW',(0,0),(-1,0),0.6,teal)]))
            story.extend([table, Spacer(1,10)])
            continue
        heading = re.match(r'^(#{1,3}) (.*)', line)
        if heading:
            story.append(p(heading[2], str(len(heading[1]))))
            if illustrated and heading[2] in INSERTIONS:
                story.append(Explanation(INSERTIONS[heading[2]]))
        elif line.startswith('> '):
            story.append(KeepTogether([p(line[2:], 'note'), Spacer(1,8)]))
        elif re.match(r'^(- |\d+\. )', line):
            story.append(p(line))
        else:
            parts = [line]
            while i+1 < len(lines) and lines[i+1].strip() and not re.match(r'^(#|\||>|<!--|- |\d+\. )', lines[i+1]):
                i += 1
                parts.append(lines[i].strip())
            story.append(p(' '.join(parts)))
        i += 1
    output = ROOT/'output/pdf'/((source.stem+'.pdf') if source_name else ('grunt-one-customer-guide-illustrated.pdf' if illustrated else 'grunt-one-customer-guide.pdf'))
    output.parent.mkdir(parents=True, exist_ok=True)
    def furniture(c, doc):
        c.setFont('Guide',8)
        c.setFillColor(colors.HexColor('#566675'))
        c.drawString(44,A4[1]-29,'GRUNT ONE  /  '+(label or 'SOLUTION AND GETTING STARTED').upper())
        c.setStrokeColor(colors.HexColor('#D9E3E4'))
        c.line(44,37,A4[0]-44,37)
        c.drawString(44,24,('Illustrated review draft' if illustrated else 'Internal review draft')+' | 21 October 2026')
        c.drawRightString(A4[0]-44,24,str(doc.page))
    SimpleDocTemplate(str(output), pagesize=A4, rightMargin=44,leftMargin=44,
        topMargin=49,bottomMargin=51,title='Grunt ONE - '+(label or 'Solution and getting started guide'),
        author='Grunt').build(story,onFirstPage=furniture,onLaterPages=furniture)
    print(output)

if __name__ == '__main__':
    build()
