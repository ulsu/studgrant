from django import template
from django.utils.safestring import mark_safe
register = template.Library()
import os

@register.filter(name='basename')
def basename(value):
    return os.path.basename(value)