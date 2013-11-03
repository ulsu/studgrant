# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.http import HttpResponse
from models import *
from forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

@login_required
def main(request):
    return show_form(request)


def show_form(request):

    try:
        account = Account.objects.get(user=request.user)
    except:
        form = AccountForm()
        plan_formset = PlanFormSet()
        pub_formset = PubFormSet()
        dip_formset = DipFormSet()
    else:
        form = AccountForm(instance=account)
        plan_formset = PlanFormSet(instance=account)
        pub_formset = PubFormSet(instance=account)
        dip_formset = DipFormSet(instance=account)

    t = loader.get_template("main/form.html")
    c = RequestContext(request, {
        'account': form,
        'plan_formset': plan_formset,
        'pub_formset': pub_formset,
        'dip_formset': dip_formset,
    })
    return HttpResponse(t.render(c))


def save(request):
    if request.method == 'POST':
        try:
            account = Account.objects.get(user=request.user)
        except:
            account_form = AccountForm(request.POST)
            if account_form.is_valid():
                account = account_form.save(commit=False)
                account.user = request.user
                account.save()
        else:
            account_form = AccountForm(request.POST, instance=account)
            if account_form.is_valid():
                account_form.save()
    return redirect('/')

