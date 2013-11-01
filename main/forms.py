# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
import datetime
from models import *
from django.forms.models import inlineformset_factory

class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            field = self.fields.get(f)
            if type(field.widget) in (forms.TextInput, forms.DateInput):
                field.widget = forms.TextInput(attrs={'placeholder': field.label})
            if type(field.widget) is forms.Textarea:
                field.widget.attrs.update({'placeholder': field.help_text})



class PlanForm(ModelForm):
    class Meta:
        model = DetailedPlan
        exclude = ['account']

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            field = self.fields.get(f)
            if type(field.widget) in (forms.TextInput, forms.DateInput):
                field.widget = forms.TextInput(attrs={'placeholder': field.label})
            if type(field.widget) is forms.Textarea:
                field.widget.attrs.update({'placeholder': field.help_text})

PlanFormSet = inlineformset_factory(Account, DetailedPlan, form=PlanForm, extra=1)