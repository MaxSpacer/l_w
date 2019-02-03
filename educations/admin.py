from django.contrib import admin
from educations.models import *

class EducationCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EducationCategory._meta.fields]
admin.site.register(EducationCategory, EducationCategoryAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.fields]
    list_display_links = ('name','id')
admin.site.register(Education, EducationAdmin)


class EducationOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in EducationOrder._meta.fields]
admin.site.register(EducationOrder, EducationOrderAdmin)


class StatusEducationOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in StatusEducationOrder._meta.fields]
admin.site.register(StatusEducationOrder, StatusEducationOrderAdmin)
