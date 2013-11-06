from django import template
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter(name='replace_n')
def replace_n(value):
    return mark_safe('<br />'.join(value.split('\n')))