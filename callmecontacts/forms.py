from .models import Callmecontacts
from django.forms import ModelForm


class CallmecontactsForm(ModelForm):
    class Meta:
        model = Callmecontacts
        fields = ['contact_name', 'contact_phone']






# class Callmecontacts(models.Model):
#     contact_name = models.CharField(max_length=32, default=None)
#     contact_phone = PhoneNumberField()
#     is_sended = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(auto_now_add=True , auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False , auto_now=True)
#
#     def __str__(self):
#         return "%s" % self.contact_name
#     class Meta:
#         verbose_name = 'Контакт для созвона'
#         verbose_name_plural = 'Контакты для созвона'
