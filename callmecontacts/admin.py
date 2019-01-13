from django.contrib import admin
from callmecontacts.models import *

# Register your models here.


class CallmecontactsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Callmecontacts._meta.fields]
admin.site.register(Callmecontacts, CallmecontactsAdmin)
