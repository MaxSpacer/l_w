from django.db import models
# from subscribers.models import Subscribers


class Subscribers(models.Model):
    subscriber_name = models.CharField(max_length=32, default=None)
    subscriber_email = models.EmailField(max_length=64, null=True)
    subscriber_phone = models.IntegerField(null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.subscribers_name
    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'
