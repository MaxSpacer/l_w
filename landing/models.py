# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Callmecontact(models.Model):
    contact_name = models.CharField(verbose_name="имя", max_length=32, default=None)
    contact_phone = PhoneNumberField(verbose_name="телефон +7XXXXXXXXX")
    is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.contact_name

    class Meta:
        verbose_name = 'Контакт для обратного звонка'
        verbose_name_plural = 'Контакты для обратного звонка'
        # app_label = 'landing'
from .signals import send_mail_on_callback
# connect them
post_save.connect(send_mail_on_callback,sender=Callmecontact,dispatch_uid="my_unique_identifier")
