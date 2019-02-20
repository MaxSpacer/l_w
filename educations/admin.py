from django.contrib import admin
from educations.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class EducationCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EducationCategory._meta.fields]
admin.site.register(EducationCategory, EducationCategoryAdmin)

class EducationFormatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EducationFormat._meta.fields]
admin.site.register(EducationFormat, EducationFormatAdmin)


class EducationResultPointInline(admin.TabularInline):
    model = EducationResultPoint


class EducationPlanPointInline(admin.TabularInline):
    model = EducationPlanPoint

class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.fields]
    list_display_links = ('name','id')
    inlines = [EducationPlanPointInline,EducationResultPointInline,]

admin.site.register(Education, EducationAdmin)

class EducationOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in EducationOrder._meta.fields]
admin.site.register(EducationOrder, EducationOrderAdmin)

# class EducationOrderInline(admin.StackedInline):
#     model = EducationOrder
#     can_delete = False
#     verbose_name_plural = 'Eduorders'
#     # readonly_fields = ('reflink','referals_qty',)
#
# class UserAdmin(BaseUserAdmin):
#     inlines = (EducationOrderInline,)
#     # inlines = (ProfileInline,)

# Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)

class StatusEducationOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in StatusEducationOrder._meta.fields]
admin.site.register(StatusEducationOrder, StatusEducationOrderAdmin)
