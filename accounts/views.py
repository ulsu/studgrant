# -*- coding: utf-8 -*-
from django.template import loader, Context, RequestContext, Template
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render
from studgrant.settings import EMAIL_FROM


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None and user.is_active:
                    if not request.POST.get('remember_me', None):
                        request.session.set_expiry(0)
                    auth.login(request, user)
            go_next = request.GET['next'] if 'next' in request.GET else '/'
            return HttpResponseRedirect(request.GET['next'])
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')

        form = LoginForm()

    return render(request, 'accounts/login.html', {
        'form': form,
        'next': request.GET['next'] if 'next' in request.GET else '/',
        })

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = User.objects.make_random_password()
            user = User.objects.create(username=form.cleaned_data['username'], email=form.cleaned_data['username'])
            user.set_password(password)
            user.save()

            subject = u'Регистрация на сайте studgrant.ulsu.ru'
            user.email_user(subject, loader.render_to_string('accounts/register_mail.html', {
                'user': user,
                'password': password,
            }), EMAIL_FROM)

            return render(request, 'accounts/register_success.html', {'user': user})
    else:
        if request.user.is_authenticated():
            return HttpResponseRedirect('/')
        form = RegisterForm()

        return render(request, 'accounts/register.html', {
            'form': form,
            'next': request.GET['next'] if 'next' in request.GET else '/',
            })
