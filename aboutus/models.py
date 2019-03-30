from django.db import models
from tinymce import HTMLField
# Create your models here.


class Aboutus(models.Model):
    title = models.CharField(max_length=128)
    content = HTMLField('Content')
    order_render = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница ABOUTUS'
        verbose_name_plural = ''

class Team(models.Model):
    name = models.CharField(max_length=128)
    service = models.CharField(max_length=128)
    image = models.ImageField(upload_to='team_images/', null=True, default=None)
    order_render = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Участник команды'
        verbose_name_plural = 'Участники команды'
