# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.filter(name='danet')
def danet(value):
    return u'Да' if value else u'Нет'