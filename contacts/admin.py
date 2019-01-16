from django.contrib import admin
from .models import Contacts

# Register your models here.


class ContactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Contacts._meta.fields]
admin.site.register(Contacts, ContactsAdmin)
