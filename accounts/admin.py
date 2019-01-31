from django.contrib import admin
from accounts.models import *

class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_display_links = ('user','id')
admin.site.register(Profile, ProfileAdmin)
