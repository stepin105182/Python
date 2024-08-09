from django import template

register = template.Library()

@register.inclusion_tag("tags_and_filters/smconnecttag.html")
def smconnect():
    return {}