# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from tinymce import HTMLField
from accounts.models import Profile
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save


class EducationCategory(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = 'Категория курсов'
		verbose_name_plural = 'Категории курсов'

class EducationFormat(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = 'Формат курсов'
		verbose_name_plural = 'Форматы курсов'



class Education(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='educations_images/', null=True, default=None)
	price = models.DecimalField(max_digits=10, decimal_places=0, default=0)
	category = models.ForeignKey(EducationCategory, on_delete=models.SET_DEFAULT, max_length=64, blank=True, null=True, default=None)
	format = models.ForeignKey(EducationFormat, on_delete=models.SET_DEFAULT, max_length=64, blank=True, null=True, default=None)
	duration = models.IntegerField(default=0)
	description = models.TextField(max_length=256,blank=True, null=True, default=None)
	content = HTMLField('Content', blank=True, null=True, default=None)
	is_disabled = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)
	publicated = models.DateTimeField(default=timezone.now, auto_now=False)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'

class StatusEducationOrder(models.Model):
    status_name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.status_name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class EducationOrder(models.Model):
    customer_name = models.CharField("имя", max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField("электронная почта", max_length=64, blank=True, null=True, default=None)
    customer_phone = PhoneNumberField("телефон +7XXXXXXXX", max_length=24, blank=True, null=True, default=None)
    education = models.ForeignKey(Education, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    # referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=False, default=1)
    # referal_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, null=True)
    status = models.ForeignKey(StatusEducationOrder, on_delete=models.SET_DEFAULT, default=1)
    is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ № %s %s" % (self.id, self.status.status_name)

    class Meta:
        verbose_name = 'Заказ курса'
        verbose_name_plural = 'Заказы курсов'

    def save(self, *args, **kwargs):
        super(EducationOrder, self).save(*args, **kwargs)


class EducationPlanPoint(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null=True, default=None)
    content = HTMLField('Content', null=True, default=None)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Пункт плана курса'
        verbose_name_plural = 'Пункты плана курса'


class EducationResultPoint(models.Model):
    title = models.CharField(max_length=64, blank=True, null=True, default=None)
    education = models.ForeignKey(Education, on_delete=models.CASCADE, blank=True, null=True, default=None)
    content = HTMLField('Content', null=True, default=None)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Результат курса'
        verbose_name_plural = 'Результаты курса'


from .signals import send_mail_on_create
post_save.connect(send_mail_on_create,sender=EducationOrder,dispatch_uid="my_unique_identifier")
