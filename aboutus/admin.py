from django.contrib import admin
from .models import Aboutus

# Register your models here.


class AboutusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Aboutus._meta.fields]
admin.site.register(Aboutus, AboutusAdmin)
