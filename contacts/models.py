from django.db import models
from tinymce import HTMLField
# Create your models here.


class Contacts(models.Model):
    title = models.CharField(max_length=128)
    content = HTMLField('Content')
    order_render = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страница Contacts'
        verbose_name_plural = 'Страницы Contacts'
