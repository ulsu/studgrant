# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
import datetime
from models import *
from widgets import *
from django.forms.models import inlineformset_factory

class AccountForm(ModelForm):
    class Meta:
        model = Account
        exclude = ['user']
        widgets = {
            'approved': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            field = self.fields.get(f)
            if type(field.widget) == forms.TextInput:
                field.widget = forms.TextInput(attrs={'placeholder': field.label})
            if type(field.widget) == forms.DateInput:
                field.widget = forms.DateInput(attrs={'placeholder': field.label, 'class': 'datepicker'})
            if type(field.widget) == forms.Textarea:
                field.widget = forms.Textarea(attrs={'placeholder': field.label})



class PlanForm(ModelForm):
    class Meta:
        model = DetailedPlan
        exclude = ['account']

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            field = self.fields.get(f)
            if type(field.widget) == forms.Textarea:
                field.widget = forms.Textarea(attrs={'class': 'plan_field'})

PlanFormSet = inlineformset_factory(Account, DetailedPlan, form=PlanForm, extra=1)


class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        exclude = ['account']

    def __init__(self, *args, **kwargs):
        super(PublicationForm, self).__init__(*args, **kwargs)
        self.fields['media_file'].widget = InlineFileInput()

PubFormSet = inlineformset_factory(Account, Publication, form=PublicationForm, extra=1)


class DiplomaForm(ModelForm):
    class Meta:
        model = Diploma
        exclude = ['account']

    def __init__(self, *args, **kwargs):
        super(DiplomaForm, self).__init__(*args, **kwargs)
        self.fields['media_file'].widget = InlineFileInput()

DipFormSet = inlineformset_factory(Account, Diploma, form=DiplomaForm, extra=1)


class CoauthorForm(ModelForm):
    class Meta:
        model = Coauthor
        exclude = ['account']

    def __init__(self, *args, **kwargs):
        super(CoauthorForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            field = self.fields.get(f)
            if type(field.widget) == forms.TextInput:
                field.widget = forms.TextInput(attrs={'placeholder': field.label, 'class': 'coauthor_field'})
            if type(field.widget) == forms.DateInput:
                field.widget = forms.DateInput(attrs={'placeholder': field.label, 'class': 'datepicker coauthor_field'})
            if type(field.widget) == forms.Textarea:
                field.widget = forms.Textarea(attrs={'placeholder': field.label, 'class': 'coauthor_field'})

CoauthorFormSet = inlineformset_factory(Account, Coauthor, form=CoauthorForm, extra=0)