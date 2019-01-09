from django.db import models
from django.utils import timezone
from tinymce import HTMLField
# Create your models here.

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
	image = models.ImageField(upload_to='event_images/', null=True, default=None)
	category = models.ForeignKey(EventCategory, on_delete=models.SET_DEFAULT, max_length=64, blank=True, null=True, default=None)
	description = models.TextField(max_length=256,blank=True, null=True, default=None)
	content = HTMLField('Content', null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)
	publicated = models.DateTimeField(default=timezone.now, auto_now=False)

	def __str__(self):
		return "%s" % self.name

	# def was_published_recently(self):
	#         return self.publicated >= timezone.now() - datetime.timedelta(days=1)

	class Meta:
		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'

# class EventImage(models.Model):
# 	event = models.ForeignKey(Event, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
# 	image = models.ImageField(upload_to='event_images/')
# 	is_main = models.BooleanField(default=False)
# 	is_active = models.BooleanField(default=True)
# 	created = models.DateTimeField(auto_now_add=True , auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False , auto_now=True)
#
# 	def __str__(self):
# 		return "%s" % self.image
#
# 	class Meta:
# 		verbose_name = 'Фотография мероприятия'
# 		verbose_name_plural = 'Фотографии мероприятий'
