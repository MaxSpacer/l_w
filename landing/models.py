# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from tinymce import HTMLField
from accounts.models import Profile


class Landpost(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=250,null=True)
    content = HTMLField('Content')
    order_render = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост для лендинга'
        verbose_name_plural = 'Посты для лендинга'


class Callmecontact(models.Model):
    contact_name = models.CharField(verbose_name="имя", max_length=32, default=None)
    contact_phone = PhoneNumberField(verbose_name="телефон +7XXXXXXXXX")
    referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.contact_name

    class Meta:
        verbose_name = 'Контакт для обратного звонка'
        verbose_name_plural = 'Контакты для обратного звонка'
        # app_label = 'landing'


class Mainformcontact(models.Model):
    contact_name = models.CharField(verbose_name="имя", max_length=32, default=None)
    contact_phone = PhoneNumberField(verbose_name="телефон +7XXXXXXXXX")
    contact_email = models.EmailField("электронная почта", max_length=64, blank=True, null=True, default=None)
    referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.contact_name

    class Meta:
        verbose_name = 'Контакт с главной страницы'
        verbose_name_plural = 'Контакты с главной страницы'


from .signals import send_mail_on_callback
from .signals import send_mail_main_form
# connect them
post_save.connect(send_mail_on_callback,sender=Callmecontact,dispatch_uid="my_unique_identifier")
post_save.connect(send_mail_main_form,sender=Mainformcontact,dispatch_uid="my_unique_identifier")
