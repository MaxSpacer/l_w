from django.contrib import admin
from modposting.models import Modpost

# Register your models here.

class ModpostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Modpost._meta.fields]
    # Register the admin class with the associated model
admin.site.register(Modpost, ModpostAdmin)
