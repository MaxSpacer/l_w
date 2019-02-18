from django.db import models
from django.utils import timezone
from tinymce import HTMLField
from accounts.models import Profile
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save



class EventCategory(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = 'Категория мероприятия'
		verbose_name_plural = 'Категории мероприятий'


class Event(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	# image = models.ImageField(upload_to='event_images/', null=True, default=None)
	category = models.ForeignKey(EventCategory, on_delete=models.SET_DEFAULT, max_length=64, blank=True, null=True, default=None)
	description = models.TextField(max_length=256,blank=True, null=True, default=None)
	content = HTMLField('Content', null=True, default=None)
	is_active = models.BooleanField(default=True)
	publicated = models.DateTimeField(default=timezone.now, auto_now=False)
	event_date = models.DateTimeField(default=timezone.now, blank=False, auto_now=False)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)


	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'


class StatusEventJoiner(models.Model):
    status_name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class EventJoiner(models.Model):
    customer_name = models.CharField("имя", max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField("электронная почта", max_length=64, blank=True, null=True, default=None)
    customer_phone = PhoneNumberField("телефон +7XXXXXXXX", max_length=24, blank=True, null=True, default=None)
    event = models.ForeignKey(Event, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    # referal = models.ForeignKey(Profile, on_delete=models.SET_DEFAULT, blank=False, default=1)
    # referal_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, null=True)
    status = models.ForeignKey(StatusEventJoiner, on_delete=models.SET_DEFAULT, default=1)
    is_emailed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ № %s %s" % (self.id, self.status.status_name)

    class Meta:
        verbose_name = 'Подписавшийся на мероприятия'
        verbose_name_plural = 'Подписавшиеся на мероприятия'


class EventImage(models.Model):
	event = models.ForeignKey(Event, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='product_images/')
	is_main = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)

	def __str__(self):
		return "%s" % self.image

	class Meta:
		verbose_name = 'Фотография продукции'
		verbose_name_plural = 'Фотографии продукции'





from .signals import send_mail_join_event
post_save.connect(send_mail_join_event,sender=EventJoiner,dispatch_uid="my_unique_identifier")
