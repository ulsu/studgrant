# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *
from forms import *


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
admin.site.register(Direction,DirectionAdmin)


class PublicationInline(admin.StackedInline):
    model = Publication
    fk_name = 'account'
    max_num = 100
    extra = 1
    formset = PubFormSet


class DiplomaInline(admin.StackedInline):
    model = Diploma
    fk_name = 'account'
    max_num = 100
    extra = 1
    formset = DipFormSet


class CoauthorInline(admin.StackedInline):
    model = Coauthor
    fk_name = 'account'
    max_num = 100
    extra = 1
    formset = CoauthorFormSet


class PlanInline(admin.StackedInline):
    model = DetailedPlan
    fk_name = 'account'
    max_num = 100
    extra = 1
    formset = PlanFormSet



class AccountAdmin(admin.ModelAdmin):
    list_display = ('admin_user', 'admin_user_fio', 'project_name', 'admin_supervisor_fio', 'admin_direction')
    inlines = [PublicationInline, DiplomaInline, CoauthorInline, PlanInline]

    fieldsets = (
        (None, {'fields': ('user','approved',)}),
        ('Студент', {'fields': ('user_fio', 'user_date', 'user_address', 'user_home_phone', 'user_mobile_phone', 'user_mail')}),
        ('Образование', {'fields': ('user_faculty', 'user_specialty', 'user_group', 'user_education_form', 'user_course')}),
        ('Научная деятельность', {'fields': ('science_area', 'project_support', 'research', 'publication_list', 'achivements')}),
        ('Научный руководитель', {'fields': ('supervisor_fio', 'contact_info', 'supervisor_faculty', 'supervisor_insitute', 'supervisor_kafedra', 'supervisor_science_area', 'publication_count', 'supervisor_achivements')}),
        ('Научный проект', {'fields': ('project_name', 'direction', 'perf_problem', 'stat_of_research', 'perf_zadel', 'shot_annotation', 'goals_and_objectives', 'proposed_methods', 'scientific_results')}),
    )


admin.site.register(Account, AccountAdmin)