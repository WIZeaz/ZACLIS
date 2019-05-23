from django import template
from markdown import markdown
#from markdown import markdown

register=template.Library()

@register.filter
def toMarkdown(s):
    return markdown(s)

@register.filter
def toBrief(s):
    ed=0
    for i in range(0,5):
        ed=s.find('</p>',ed+1)
        if ed==-1:
            return s
        elif ed>=100:
            break
    ed=ed+4
    return s[:ed]+"<p> ...... </p>"
    
@register.filter
def mod3(s):
    if s%3==0:
        return True
    return False