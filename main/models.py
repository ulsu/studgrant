# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from managers import *


class Direction(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название", blank=True, null=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'направление'
        verbose_name_plural = 'направления'


class Account(models.Model):
    user = models.ForeignKey('accounts.User', verbose_name='Пользователь', related_name='account')
    approved = models.BooleanField(default=False)
    user_fio = models.CharField(max_length=255, verbose_name='ФИО', blank=True, null=True)
    user_date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    user_address = models.CharField(max_length=255, verbose_name='Почтовый адрес', blank=True, null=True)
    user_home_phone = models.CharField(max_length=255, verbose_name='Домашний телефон', blank=True, null=True)
    user_mobile_phone = models.CharField(max_length=255, verbose_name='Сотовый телефон', blank=True, null=True)
    user_mail = models.CharField(max_length=255, verbose_name='Электронная почта', blank=True, null=True)

    user_faculty = models.CharField(max_length=255, verbose_name='Факультет', blank=True, null=True)
    user_specialty = models.CharField(max_length=255, verbose_name='Специальность', blank=True, null=True)
    user_group = models.CharField(max_length=255, verbose_name='Группа', blank=True, null=True)
    user_education_form = models.CharField(max_length=255, verbose_name='Форма обучения', blank=True, null=True)
    user_course = models.CharField(max_length=255, verbose_name='Курс', blank=True, null=True)

    science_area = models.TextField(verbose_name='Область научных интересов', help_text='Ключевые слова, не более 15', blank=True, null=True)
    project_support = models.TextField(verbose_name='Поддержка проектов заявителя в форме грантов', help_text='Для каждого проекта обязательно укажите название фонда, год, номер регистрации и название проекта', blank=True, null=True)
    research = models.TextField(verbose_name='Участие в научно-исследовательской работе', help_text='Направление, творческий коллектив', blank=True, null=True)
    publication_list = models.TextField(verbose_name='Список публикаций', blank=True, null=True)
    achivements = models.TextField(verbose_name='Наличие наград, дипломов, результаты участия в конкурсах студенческих работ, олимпиадах, конференциях', blank=True, null=True)

    # Данные о научном руководителе
    supervisor_fio = models.CharField(max_length=255, verbose_name='ФИО', blank=True, null=True)
    contact_info = models.TextField(verbose_name='Контактная информация', help_text='Контактная информация', blank=True, null=True)
    supervisor_faculty = models.CharField(max_length=255, verbose_name='Факультет', blank=True, null=True)
    supervisor_insitute = models.CharField(max_length=255, verbose_name='Институт', blank=True, null=True)
    supervisor_kafedra = models.CharField(max_length=255, verbose_name='Кафедра', blank=True, null=True)
    supervisor_science_area = models.TextField(verbose_name='Область научных интересов', help_text='Ключевые слова, не более 15', blank=True, null=True)
    publication_count = models.CharField(max_length=255, verbose_name='Общее число публикаций', blank=True, null=True)
#     Наличие выполняемых научно-исследовательских работ в рамках грантов, хоз. договоров
    supervisor_achivements = models.BooleanField(verbose_name='Наличие выполняемых научно-исследовательских работ в рамках грантов, хоз. договоров',)
    # Форма научного проекта
    project_name = models.TextField(verbose_name="Название проекта", blank=True, null=True)
    direction = models.ForeignKey('Direction', blank=True, null=True, related_name='accounts', verbose_name="Направление конкурса (в соответствии с объявленными номинациями)", )
    perf_problem = models.TextField(verbose_name="Научная проблема, на решение которой направлен проект, ее актуальность, фундаментальная и практическая ценность. Место планируемых работ в обозначенной тематике", blank=True, null=True)
    stat_of_research = models.TextField(verbose_name="Современное состояние исследований в данной области науки", blank=True, null=True)
    perf_zadel = models.TextField(verbose_name="Имеющийся у исполнителя научный задел по предлагаемому проекту: полученные ранее результаты (с оценкой степени оригинальности), разработанные методы (с оценкой степени новизны)", blank=True, null=True)
    shot_annotation = models.TextField(verbose_name="Краткая аннотация (не более 0,5 стр.)", blank=True, null=True)
    goals_and_objectives = models.TextField(verbose_name="Цели и задачи реализации проекта", blank=True, null=True)
    proposed_methods = models.TextField(verbose_name="Предлагаемые методы и подходы (с оценкой степени новизны)", blank=True, null=True)
    scientific_results = models.TextField(verbose_name="Ожидаемые научные результаты", help_text="Форма изложения должна дать возможность провести экспертизу результатов", blank=True, null=True)
    objects = AccountManager()

    def admin_direction(self):
        return self.direction
    admin_direction.short_description = 'Направление'

    def admin_user(self):
        return self.user
    admin_user.short_description = 'Логин'

    def admin_user_fio(self):
        return self.user_fio
    admin_user_fio.short_description = 'Студент'

    def admin_supervisor_fio(self):
        return self.supervisor_fio
    admin_supervisor_fio.short_description = 'Научный руководитель'


    def report_path(self, filename):
        return '%s/report/%s' % (self.id, filename)

    report = models.FileField(verbose_name="Отзыв научного руководителя о планируемой работе", blank=True, null=True, upload_to=report_path)

    def __unicode__(self):
        return self.user_fio

    class Meta:
        verbose_name = 'форма'
        verbose_name_plural = 'формы'

class Coauthor(models.Model):
    account = models.ForeignKey(Account)
    fio = models.CharField(max_length=255, verbose_name='ФИО', blank=True, null=True)
    date = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    place = models.TextField(verbose_name="Место учёбы (факультет, специальность, курс, группа, форма обучения: бюджетная или внебюджетная)",help_text="Место учёбы (факультет, специальность, курс, группа, форма обучения: бюджетная или внебюджетная)", blank=True, null=True)
    information = models.TextField(verbose_name='Почтовый адрес, телефон, электронный адрес', help_text='Почтовый адрес, телефон, электронный адрес', blank=True, null=True)

    def __unicode__(self):
        return self.fio

    class Meta:
        verbose_name = 'соавтор'
        verbose_name_plural = 'соавторы'


class DetailedPlan(models.Model):
    account = models.ForeignKey(Account)
    dates = models.TextField(verbose_name="Сроки проведения", blank=True, null=True)
    content = models.TextField(verbose_name="Содержание работ", blank=True, null=True)
    place = models.TextField(verbose_name="Место проведения", blank=True, null=True)

    def __unicode__(self):
        return self.account.user_fio

    class Meta:
        verbose_name = 'этап'
        verbose_name_plural = 'этапы плана'

class Publication(models.Model):
    account = models.ForeignKey(Account, related_name='publications')

    def path(self, filename):
        return '%s/publications/%s' % (self.account_id, filename)
    media_file = models.FileField(upload_to=path, verbose_name='Прикреплённый файл')

    def __unicode__(self):
        return self.media_file

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'


class Diploma(models.Model):
    account = models.ForeignKey(Account, related_name='diplomas')

    def path(self, filename):
        return '%s/diplomas/%s' % (self.account_id, filename)
    media_file = models.FileField(upload_to=path, verbose_name='Прикреплённый файл')

    def __unicode__(self):
        return self.media_file

    class Meta:
        verbose_name = 'награда, диплом'
        verbose_name_plural = 'награды, дипломы'