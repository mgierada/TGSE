from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.template.defaultfilters import stringfilter
import re

register = template.Library()


# @register.filter(needs_autoescape=True)
# @stringfilter
# def highlight(value, search_term, autoescape=True):
#     return mark_safe(value.replace(search_term, "<span class='highlight'>%s</span>" % search_term))

@register.filter(needs_autoescape=True)
def highlight(text, sterm, autoescape=None):
    if autoescape:
        esc = conditional_escape
    else:
        def esc(x): return x
    pattern = re.compile('(%s)' % esc(sterm), re.IGNORECASE)
    result = pattern.sub(r'<strong class="yellow">\1</strong>', text)
    return mark_safe(result)
