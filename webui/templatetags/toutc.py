from django import template

register = template.Library()

@register.filter
def to_utc(value):  
    val = int(value)*1000
    return str(val)

