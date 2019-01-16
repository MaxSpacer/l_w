from django.db import models
from django.utils import timezone
from tinymce import HTMLField
# Create your models here.


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


class Education(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='educations_images/', null=True, default=None)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	category = models.ForeignKey(EducationCategory, on_delete=models.SET_DEFAULT, max_length=64, blank=True, null=True, default=None)
	description = models.TextField(max_length=256,blank=True, null=True, default=None)
	content = HTMLField('Content', null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)
	publicated = models.DateTimeField(default=timezone.now, auto_now=False)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = 'Курс'
		verbose_name_plural = 'Курсы'
