# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.http import HttpResponse
from models import *

def main(request):
    return show_form(request)

def show_form(request):
    t = loader.get_template("main/form.html")
    c = RequestContext(request, {})
    return HttpResponse(t.render(c))
