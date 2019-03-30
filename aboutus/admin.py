from django.contrib import admin
from .models import *

# Register your models here.


class AboutusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Aboutus._meta.fields]
    # list_display_links = ('user','id')
admin.site.register(Aboutus, AboutusAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Team._meta.fields]
    # list_display_links = ('user','id')
admin.site.register(Team, TeamAdmin)
