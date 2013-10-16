# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.http import HttpResponse
from models import *
from forms import *
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    return show_form(request)


def show_form(request):
    account = AccountForm()
    t = loader.get_template("main/form.html")
    c = RequestContext(request, {'account': account})
    return HttpResponse(t.render(c))