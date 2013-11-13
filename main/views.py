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
from django.http import Http404


def mediaserver(request, path):
    if request.user.is_superuser:
        return serve(request, path, settings.MEDIA_ROOT)


@login_required
def main(request):
    if request.user.is_secretary or request.user.is_superuser:
        return show_table(request)
    else:
        if Account.objects.filter(user=request.user).exists() and \
                        Account.objects.get(user=request.user).approved == True:
            return show_approved_info(request)
        else:
            return show_form(request)


def show_form(request):
    account, created = Account.objects.get_or_create(user=request.user)
    return load_form(request, account)

def edit_form(request, id):
    try:
        account = Account.objects.get(pk=id)
    except Account.DoesNotExist:
        raise Http404

    if request.user.is_superuser:
        return load_form(request, account)
    elif request.user.is_secretary:
        if request.user.directions.filter(pk=account.direction_id).count():
            return load_form(request, account)
        else:
            raise Http404
    else:
        raise Http404

def load_form(request, account):
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
        if 'account_id' in request.POST and (request.user.is_superuser or request.user.is_secretary):
            account = Account.objects.get(pk=int(request.POST['account_id']))
            if not request.user.is_superuser and not request.user.directions.filter(pk=account.direction_id).count():
                account, created = Account.objects.get_or_create(user=request.user)
        else:
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

def show_approved_info(request):
    account = get_object_or_404(Account, user=request.user.id)
    t = loader.get_template("main/approved.html")
    c = RequestContext(request, {'account': account})
    return HttpResponse(t.render(c))


def log(request, var):
    t = loader.get_template("log.html")
    c = RequestContext(request, {'var': var})
    return HttpResponse(t.render(c))