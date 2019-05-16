from django import template
from markdown import markdown
#from markdown import markdown

register=template.Library()

@register.filter
def toMarkdown(s):
    return markdown(s)
