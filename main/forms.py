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