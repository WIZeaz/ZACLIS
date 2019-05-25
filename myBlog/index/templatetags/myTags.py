from django import template
from markdown import markdown
from random import randint
#from markdown import markdown

register=template.Library()

@register.filter
def toMarkdown(s):
    return markdown(s,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

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
def mod4(s):
    if s%4==0:
        return True
    return False

@register.filter
def randomTagStyle(tagname):
    l=['default','primary','success','info','warning','danger']
    return '<span class="label label-'+l[randint(0,5)]+'"><a class="tag" href="/tag/'+tagname+'">'+tagname+'</a></span>'