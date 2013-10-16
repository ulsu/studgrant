# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User


class Account(models.Model):
    # data user
    user = models.ForeignKey(User, verbose_name='Пользователь')
    user_fio = models.CharField(max_length=255, verbose_name='ФИО')
    user_date = models.DateField(verbose_name='Дата рождения')
    user_address = models.CharField(max_length=255, verbose_name='Почтовый адрес')
    user_home_phone = models.CharField(max_length=255, verbose_name='Домашний телефон')
    user_mobile_phone = models.CharField(max_length=255, verbose_name='Сотовый телефон')
    user_mail = models.CharField(max_length=255, verbose_name='Электронная почта')
#     Mesto ucheb
    user_faculty = models.CharField(max_length=255, verbose_name='Факультет')
    user_specialty = models.CharField(max_length=255, verbose_name='Специальность')
    user_group = models.CharField(max_length=255, verbose_name='Группа')
    user_education_form = models.CharField(max_length=255, verbose_name='Форма обучения')
    user_course = models.CharField(max_length=255, verbose_name='Курс')
#     Область научных интересов
    science_area = models.TextField(verbose_name='Область научных интересов', help_text='Ключевые слова, не более 15')
#     Поддержка проектов заявителя в форме грантов
    project_support = models.TextField(verbose_name='Поддержка проектов заявителя в форме грантов', help_text='Для каждого проекта обязательно укажите название фонда, год, номер регистрации и название проекта')
#     Участие в научно-исследовательской работе
    research = models.TextField(verbose_name='Участие в научно-исследовательской работе', help_text='Направление, творческий коллектив')
#     Список публикаций
    publication_list = models.TextField(verbose_name='Список публикаций')
# Наличие наград, дипломов, результаты участия в конкурсах студенческих работ, олимпиадах, конференциях
    achivements = models.TextField(verbose_name='Наличие наград, дипломов, результаты участия в конкурсах студенческих работ, олимпиадах, конференциях')
#     Данные о научном руководителе
    supervisor_fio = models.CharField(max_length=255, verbose_name='ФИО')
    contact_info = models.TextField(verbose_name='Контактная информация', help_text='Контактная информация')
    supervisor_faculty = models.CharField(max_length=255, verbose_name='Факультет')
    supervisor_insitute = models.CharField(max_length=255, verbose_name='Институт')
    supervisor_kafedra = models.CharField(max_length=255, verbose_name='Кафедра')
    supervisor_science_area = models.TextField(verbose_name='Область научных интересов', help_text='Ключевые слова, не более 15')
    publication_count = models.CharField(max_length=255, verbose_name='Общее число публикаций')
#     Наличие выполняемых научно-исследовательских работ в рамках грантов, хоз. договоров
    supervisor_achivements = models.BooleanField(verbose_name='Наличие выполняемых научно-исследовательских работ в рамках грантов, хоз. договоров')

