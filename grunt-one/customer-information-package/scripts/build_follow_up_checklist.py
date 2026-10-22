"""Render the complete maintained information list, including every table cell."""
from pathlib import Path
import re
import html
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'drafts/grunt-one-missing-information.md'
text = source.read_text(encoding='utf-8-sig')
rows = [[v.strip() for v in line.strip('|').split('|')] for line in text.splitlines() if line.startswith('| [ ] |')]
assert len(rows) == 8
for name, file in [('Guide', 'arial.ttf'), ('GuideBold', 'arialbd.ttf')]:
    pdfmetrics.registerFont(TTFont(name, 'C:/Windows/Fonts/' + file))
pdfmetrics.registerFontFamily('Guide', normal='Guide', bold='GuideBold', italic='Guide', boldItalic='GuideBold')
ink, teal = colors.HexColor('#182330'), colors.HexColor('#126B70')
styles = {
    'body': ParagraphStyle('body', fontName='Guide', fontSize=10, leading=14, textColor=ink, spaceAfter=7),
    'title': ParagraphStyle('title', fontName='GuideBold', fontSize=22, leading=27, textColor=teal, spaceAfter=12),
    'section': ParagraphStyle('section', fontName='GuideBold', fontSize=15, leading=20, textColor=teal, spaceBefore=12, spaceAfter=12, keepWithNext=True),
    'task': ParagraphStyle('task', fontName='GuideBold', fontSize=12, leading=16, textColor=teal, spaceBefore=8, spaceAfter=8),
    'meta': ParagraphStyle('meta', fontName='Guide', fontSize=9, leading=12, textColor=ink, spaceAfter=7),
}
def para(s, kind='body'):
    s = html.escape(s.replace('–','-').replace('—','-'))
    s = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<link href="\2" color="#126B70"><u>\1</u></link>', s)
    s = re.sub(r'`([^`]+)`', r'\1', s)
    return Paragraph(s, styles[kind])

story=[]
lines=text.splitlines()
i=0
while i < len(lines):
    line=lines[i].strip()
    if not line:
        i+=1
        continue
    if line.startswith('# '):
        story.append(para(line[2:], 'title'))
    elif line.startswith('## '):
        if line.startswith('## Detailed requests:') or line.startswith('## Evidence update') or line.startswith('## Efficient way'):
            story.append(PageBreak())
        story.append(para(line[3:],'section'))
    elif line.startswith('|'):
        table=[]
        while i < len(lines) and lines[i].strip().startswith('|'):
            cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
            if not all(re.fullmatch(r':?-+:?', c) for c in cells):
                table.append(cells)
            i+=1
        headers=table[0]
        for row in table[1:]:
            if len(row)==5:
                done,action,owner,result,ids=row
                match=re.match(r'\*\*(.*?)\*\*\s*(.*)',action)
                title,detail=match.groups()
                block=[para(done+' '+title,'task'),para(detail),para('**'+headers[2]+':** '+owner+' | **'+headers[4]+':** '+ids,'meta'),para('**'+headers[3]+':** '+result),para('Assigned to: ____________________    Target date: ______________','meta'),Spacer(1,7)]
            else:
                ident,needed,owner=row
                block=[para(ident,'task'),para('**'+headers[1]+':** '+needed),para('**'+headers[2]+':** '+owner,'meta'),Spacer(1,4)]
            story.append(KeepTogether(block))
        continue
    else:
        story.append(para(line))
    i+=1

out=ROOT/'output/pdf/grunt-one-follow-up-checklist.pdf'
def furniture(c,doc):
    c.setFont('Guide',8);c.setFillColor(colors.HexColor('#566675'))
    c.drawString(44,A4[1]-29,'GRUNT ONE / INTERNAL FOLLOW-UP')
    c.setStrokeColor(colors.HexColor('#D9E3E4'));c.line(44,37,A4[0]-44,37)
    c.drawString(44,24,'Internal working checklist | 22 October 2026')
    c.drawRightString(A4[0]-44,24,str(doc.page))
SimpleDocTemplate(str(out),pagesize=A4,leftMargin=44,rightMargin=44,topMargin=49,bottomMargin=51,title='Grunt ONE - Prioritized follow-up checklist',author='Grunt').build(story,onFirstPage=furniture,onLaterPages=furniture)
print(out)
