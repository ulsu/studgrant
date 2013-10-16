# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
import datetime
from models import Account

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