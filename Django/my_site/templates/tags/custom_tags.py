from django import template

register = template.Library()

@register.inclusion_tag("tags/smconnecttag.html")
def smconnect():
    return {}