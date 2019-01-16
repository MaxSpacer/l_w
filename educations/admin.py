from django.contrib import admin
from educations.models import *
# Register your models here.

class EducationCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EducationCategory._meta.fields]
admin.site.register(EducationCategory, EducationCategoryAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.fields]
    list_display_links = ('name','id')
admin.site.register(Education, EducationAdmin)
