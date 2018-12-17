from django.db import models
from tinymce import HTMLField
# Create your models here.


class Modpost(models.Model):
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
        verbose_name = 'Блок для мод.постинга'
        verbose_name_plural = 'Блоки для мод.постинга'

# class Modpost(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField(max_length=250,null=True)
#     content = HTMLField('Content')
#     order_render = models.IntegerField(default=0)
#     is_active = models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Блок для лендинга'
#         verbose_name_plural = 'Блоки для лендинга'
