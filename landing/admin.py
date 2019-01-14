from django.contrib import admin
from .models import Callmecontact

# Register your models here.


class CallmecontactAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Callmecontact._meta.fields]
admin.site.register(Callmecontact, CallmecontactAdmin)
