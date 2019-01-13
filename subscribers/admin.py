from django.contrib import admin
from subscribers.models import *

# Register your models here.


class SubscribersAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscribers._meta.fields]
admin.site.register(Subscribers, SubscribersAdmin)
