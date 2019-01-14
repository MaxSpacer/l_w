from phonenumber_field.modelfields import PhoneNumberField
from django.db import models


class Callmecontact(models.Model):
    contact_name = models.CharField(verbose_name="Имя", max_length=32, default=None)
    contact_phone = PhoneNumberField(verbose_name="Телефон")
    is_sended = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.contact_name
    class Meta:
        verbose_name = 'Контакт для созвона'
        verbose_name_plural = 'Контакты для созвона'
