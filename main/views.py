# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.http import HttpResponse
from models import *
from forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.static import serve
from studgrant import settings
from django.shortcuts import get_object_or_404
from pdf_generator.views import generate_pdf


def mediaserver(request, path):
    if request.user.is_superuser:
        return serve(request, path, settings.MEDIA_ROOT)


@login_required
def main(request):
    if request.user.is_secretary or request.user.is_superuser:
        return show_table(request)
    else:
        return show_form(request)


def show_form(request):
    account, created = Account.objects.get_or_create(user=request.user)
    form = AccountForm(instance=account)
    plan_formset = PlanFormSet(instance=account)
    pub_formset = PubFormSet(instance=account)
    dip_formset = DipFormSet(instance=account)
    coauthor_formset = CoauthorFormSet(instance=account)

    t = loader.get_template("main/form.html")
    c = RequestContext(request, {
        'account': form,
        'plan_formset': plan_formset,
        'pub_formset': pub_formset,
        'dip_formset': dip_formset,
        'coauthor_formset': coauthor_formset
    })
    return HttpResponse(t.render(c))


def save(request):
    if request.method == 'POST':
        account, created = Account.objects.get_or_create(user=request.user)
        account_form = AccountForm(request.POST, request.FILES, instance=account)
        if account_form.is_valid():
            account = account_form.save()

        plan_formset = PlanFormSet(request.POST, instance=account)
        if plan_formset.is_valid():
            plan_formset.save()

        pub_formset = PubFormSet(request.POST, request.FILES, instance=account)
        if pub_formset.is_valid():
            pub_formset.save()

        dip_formset = DipFormSet(request.POST, request.FILES, instance=account)
        if dip_formset.is_valid():
            dip_formset.save()

        coauthor_formset = CoauthorFormSet(request.POST, instance=account)
        if coauthor_formset.is_valid():
            coauthor_formset.save()
    return redirect('/')

def pdf(request, id):
    account = get_object_or_404(Account, pk=id)
    if request.user.is_staff or request.user == account.user:
        form = AccountForm(instance=account)
        context = {
            'account': form,
            'plan': PlanFormSet(instance=account)
        }
        return generate_pdf(request, context)

def show_table(request):
    directions = Direction.objects.all()

    t = loader.get_template("main/accounts_list.html")
    c = RequestContext(request, {'directions': directions})
    return HttpResponse(t.render(c))

