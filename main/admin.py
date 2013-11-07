# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Publication, Account
from forms import PubFormSet

class PublicationInline(admin.StackedInline):
    model = Publication
    fk_name = 'account'
    max_num = 1
    extra = 0
    formset = PubFormSet



class AccountAdmin(admin.ModelAdmin):
    title = ('user','user_fio', 'user_mail')
    inlines = [PublicationInline, ]

    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Студент', {'fields': ('user_fio', 'user_date', 'user_address', 'user_home_phone', 'user_mobile_phone', 'user_mail')}),
        ('Образование', {'fields': ('user_faculty', 'user_specialty', 'user_group', 'user_education_form', 'user_course')}),
        ('Научная деятельность', {'fields': ('science_area', 'project_support', 'research', 'publication_list', 'achivements')}),
        ('Научный руководитель', {'fields': ('supervisor_fio', 'contact_info', 'supervisor_faculty', 'supervisor_insitute', 'supervisor_kafedra', 'supervisor_science_area', 'publication_count', 'supervisor_achivements')}),
        ('Научный проект', {'fields': ('project_name', 'direction', 'perf_problem', 'stat_of_research', 'perf_zadel', 'shot_annotation', 'goals_and_objectives', 'proposed_methods', 'scientific_results')}),
    )


admin.site.register(Account, AccountAdmin)