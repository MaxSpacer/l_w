# -*- coding: utf-8 -*-

from django.db import models
from django.db.models.signals import post_save


class MemberPreference(models.Model):
    order = models.IntegerField("Порядок следования", default=0)
    title = models.CharField(max_length=128, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Преференции'
        verbose_name_plural = 'Что дает членство клуба'


class Bill(models.Model):
    order = models.IntegerField("Порядок следования",default=0)
    broker_image = models.ImageField(upload_to='broker_images/', null=True, default=None)
    duration = models.TextField(max_length=128,blank=True, null=True, default=None)
    result = models.TextField(max_length=128,blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.broker_image

    class Meta:
        verbose_name = 'Брокер'
        verbose_name_plural = 'Брокеры'

#
# class StatusInvestionOrder(models.Model):
#     status_name = models.CharField(max_length=24, blank=True, null=True, default=None)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True , auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False , auto_now=True)
#
#     def __str__(self):
#         return "%s" % self.status_name
#
#     class Meta:
#         verbose_name = 'Статус заказа'
#         verbose_name_plural = 'Статусы заказа'
#
#
# class InvestionOrder(models.Model):
#     customer_name = models.CharField("имя", max_length=64, blank=True, null=True, default=None)
#     customer_email = models.EmailField("электронная почта", max_length=64, blank=True, null=True, default=None)
#     customer_phone = PhoneNumberField("телефон +7XXXXXXXX", max_length=24, blank=True, null=True, default=None)
#     investion = models.ForeignKey(Investion, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
#     referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
#     # referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=False, default=1)
#     # referal_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, null=True)
#     status = models.ForeignKey(StatusInvestionOrder, on_delete=models.SET_DEFAULT, default=1)
#     is_emailed = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return "Заказ № %s %s" % (self.id, self.status.status_name)
#
#     class Meta:
#         verbose_name = 'Заказ инвестиции'
#         verbose_name_plural = 'Заказы инвестиций'
#
#     def save(self, *args, **kwargs):
#         super(InvestionOrder, self).save(*args, **kwargs)


# from .signals import send_mail_on_create
# post_save.connect(send_mail_on_create,sender=InvestionOrder,dispatch_uid="my_unique_identifier")
