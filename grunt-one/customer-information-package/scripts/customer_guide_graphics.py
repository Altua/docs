"""Vector explanations; claims and qualifications follow the Markdown master."""
from reportlab.platypus import Flowable, Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
import math

TEAL = '#126B70'
INK = '#182330'
PALE = '#EEF5F4'
AMBER = '#FFF2D9'

class Explanation(Flowable):
    def __init__(self, kind):
        super().__init__()
        self.kind = kind
        self.width = 495
        self.height = dict(workflow=242, routes=328, hosted=342,
            customer=382, identity=247, sharing=226, setup=280)[kind]
        self.spaceAfter = 14

    def text(self, x, y, w, text, size=9, bold=False, color=INK):
        p = Paragraph(text, ParagraphStyle('diagram',
            fontName='GuideBold' if bold else 'Guide', fontSize=size,
            leading=size+3, textColor=colors.HexColor(color)))
        _, h = p.wrap(w, 1000)
        p.drawOn(self.canv, x, self.height-y-h)
        return h

    def box(self, x, y, w, h, title, body='', fill=PALE, dashed=False):
        c = self.canv
        c.saveState()
        c.setFillColor(colors.HexColor(fill))
        c.setStrokeColor(colors.HexColor('#BACDCE'))
        if dashed: c.setDash(4,3)
        c.roundRect(x,self.height-y-h,w,h,7,fill=1,stroke=1)
        c.restoreState()
        used = self.text(x+10,y+8,w-20,title,9.5,True)
        if body: self.text(x+10,y+12+used,w-20,body,8.5)

    def arrow(self, x1,y1,x2,y2,dashed=False):
        c=self.canv
        a=math.atan2(y2-y1,x2-x1)
        c.saveState()
        c.setStrokeColor(colors.HexColor(TEAL))
        c.setLineWidth(1.2)
        if dashed: c.setDash(4,3)
        c.line(x1,self.height-y1,x2,self.height-y2)
        c.setDash()
        for offset in [-0.48,0.48]:
            c.line(x2,self.height-y2,x2-5*math.cos(a+offset),
                self.height-y2+5*math.sin(a+offset))
        c.restoreState()

    def draw(self):
        k=self.kind
        self.text(0,0,495,{
            'workflow':'FROM A QUESTION TO A DELIVERABLE',
            'routes':'TWO WAYS TO WORK WITH AI',
            'hosted':'GRUNT-HOSTED: EXTERNAL ASSISTANT ROUTE',
            'customer':'CUSTOMER-HOSTED: INTENDED ARCHITECTURE',
            'identity':'ACCOUNT ACCESS TO SAVED ASSETS',
            'sharing':'A VIEW LINK ALSO EXPOSES DATA',
            'setup':'FROM ACCESS TO FIRST SUCCESS'
        }[k],8,True,TEAL)
        if k=='workflow':
            for x,title,body in [
                (0,'1. Approved data','Figures + business question'),
                (127,'2. AI creation','Explore and build a first version'),
                (254,'3. Human editing','Check data; refine the visual'),
                (381,'4. Deliver','PowerPoint or web report')]:
                self.box(x,29,114,88,title,body)
            for x in [114,241,368]: self.arrow(x+2,72,x+11,72)
            self.box(127,137,368,55,'Structured Grunt assets',
                'Data, formatting rules and saved versions support reuse.')
            self.arrow(184,117,184,137)
            self.arrow(311,117,311,137)
            self.text(0,207,495,'Workflow overview. Enabled tools and output behavior are specified in the evaluation scope.',8.5)
        elif k=='routes':
            cols=[
                ('Inside PowerPoint','Grunt AI pane','Grunt AI service + model provider','Preview, then Accept or Skip','Requires enabled Grunt AI access.'),
                ('Inside an assistant','Compatible external assistant','Grunt MCP + asset services','Create, inspect and revise assets','Requires supported client and Grunt access.')]
            for j,(title,a,b,out,note) in enumerate(cols):
                x=j*260
                self.text(x,29,235,title,10,True)
                self.box(x,51,235,40,a,fill='#F5F7F8')
                self.arrow(x+117,92,x+117,105)
                self.box(x,108,235,43,b)
                self.arrow(x+117,152,x+117,165)
                self.box(x,168,235,43,out,fill='#F5F7F8')
                self.text(x+3,222,229,note,8.5)
            self.box(0,263,495,53,'IN DEVELOPMENT: live control of an open PowerPoint deck',
                'A separate connection; creating MCP assets does not provide live deck control.',fill=AMBER,dashed=True)
        elif k=='hosted':
            self.box(0,31,139,80,'Customer','User + approved data<br/>Browser editor access',fill='#F5F7F8')
            self.box(179,31,139,80,'External AI provider','Assistant account<br/>Prompts and tool results',fill='#F1F0F9')
            self.box(358,31,137,80,'Grunt-operated','MCP + asset services<br/>Storage and rendering')
            self.arrow(140,65,177,65)
            self.arrow(319,65,356,65)
            self.text(141,80,36,'Data + prompt',7)
            self.text(320,80,36,'Tool calls',7)
            self.arrow(358,126,249,126)
            self.arrow(249,126,249,112)
            self.text(179,139,309,'Returned results: previews, links and requested underlying data.',8.5)
            self.arrow(70,112,70,179)
            self.arrow(70,179,426,179)
            self.arrow(426,179,426,112)
            self.text(81,184,405,'Browser path: open asset, edit content and save revisions.',8.5)
            self.box(0,220,238,67,'Authorization','User/client obtains permission through Grunt authentication; MCP calls carry access tokens.',fill='#F5F7F8')
            self.box(252,220,243,67,'Selected outputs','PowerPoint or web report uses the accepted result through the enabled output workflow.',fill='#F5F7F8')
            self.text(0,302,495,'Logical boundaries, not a network allowlist. Grunt AI in PowerPoint has a separate Grunt-managed AI processing route.',8.5)
        elif k=='customer':
            self.box(0,27,495,42,'IN DEVELOPMENT - evaluation scope to be confirmed',fill=AMBER,dashed=True)
            self.box(0,84,310,148,'Customer-operated environment',
                'User / browser + Grunt content services',fill=PALE,dashed=True)
            self.box(14,132,282,83,'MCP server + Web Editor',
                'Asset storage, saved history, rendering and exports<br/>Browser edits and revisions remain within this service boundary.',fill='#FFFFFF')
            self.box(352,84,143,93,'External AI provider',
                'Approved assistant<br/>Prompts / data and returned tool results',fill='#F1F0F9')
            self.arrow(351,145,311,145)
            self.arrow(311,164,351,164)
            self.text(318,184,177,'Approved network path required',8)
            self.box(0,251,153,80,'Grunt services',
                'Entitlement verification + aggregate usage reporting',fill='#F5F7F8')
            self.box(171,251,153,80,'Release distribution',
                'Installation / administrator obtains approved releases',fill='#F5F7F8')
            self.box(342,251,153,80,'Identity service',
                'User authentication depends on the deployment configuration',fill='#F5F7F8')
            self.arrow(76,233,76,249)
            self.arrow(248,249,248,233)
            self.text(0,347,495,'External AI processing and service connections remain. Initial customer hosting is not fully disconnected; hosting Grunt does not also host the AI model.',8.5)
        elif k=='identity':
            for x,title,first,second,last in [
                (0,'PERSONAL ACCESS','Person + compatible assistant','OAuth sign-in and authorization','User-owned assets'),
                (260,'ORGANIZATION ACCESS','Organization service','Authorized organization context','Organization-owned assets')]:
                self.text(x,28,235,title,9,True)
                self.box(x,50,235,40,first,fill='#F5F7F8')
                self.arrow(x+117,91,x+117,106)
                self.box(x,108,235,43,second)
                self.arrow(x+117,152,x+117,166)
                self.box(x,168,235,40,last)
            self.text(0,220,495,'Separate account access. Other organization MCP clients can access organization assets; these do not automatically appear in a personal asset list.',8.5)
        elif k=='sharing':
            self.box(0,49,145,66,'Permanent view link','Access for anyone holding the link')
            self.arrow(146,65,230,65)
            self.arrow(146,99,230,136)
            self.box(233,31,262,61,'Rendered visual','The chart or table image')
            self.box(233,108,262,61,'Underlying data','The values behind the visual')
            self.box(0,187,495,36,'No expiry; links cannot currently be revoked',fill=AMBER)
        elif k=='setup':
            steps=[
                ('1','Activate access','Administrator + Grunt/CS','Required products, users and subscriptions'),
                ('2','Prepare environment','Customer IT','Approved software, endpoints and data'),
                ('3','Configure access','Administrator + Grunt/CS','Users, product access and asset ownership'),
                ('4','Connect tools','User','Sign in to Grunt; discover tools'),
                ('5','Complete first task','Users + IT + Grunt/CS','Create, inspect, edit, deliver and check access')]
            for j,(n,title,owner,detail) in enumerate(steps):
                y=29+j*45
                self.box(0,y,32,32,n)
                if j<4:self.arrow(16,y+33,16,y+42)
                self.text(46,y,182,title,10,True)
                self.text(46,y+17,182,owner,8,False,TEAL)
                self.text(246,y+4,249,detail,9)
            self.text(0,260,495,'Roles shown are a typical setup sequence; internal responsibilities may vary.',8)

INSERTIONS = {
    'A workflow from data to a finished deliverable':'workflow',
    'The three AI routes':'routes',
    'Grunt-hosted':'hosted',
    'Customer-hosted':'customer',
    'Per-user sign-in or organization credentials':'identity',
    'What sharing a link permits':'sharing',
    'Getting started':'setup',
}
