from django.contrib import admin
from investions.models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class InvestionCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InvestionCategory._meta.fields]
admin.site.register(InvestionCategory, InvestionCategoryAdmin)

class InvestionFormatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in InvestionFormat._meta.fields]
admin.site.register(InvestionFormat, InvestionFormatAdmin)


class InvestionResultPointInline(admin.TabularInline):
    model = InvestionResultPoint
# admin.site.register(InvestionResultPoint, InvestionResultPointAdmin)

class InvestionPlanPointInline(admin.TabularInline):
    model = InvestionPlanPoint
# admin.site.register(InvestionPlanPoint, InvestionPlanPointAdmin)

class InvestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Investion._meta.fields]
    list_display_links = ('name','id')
    inlines = [InvestionPlanPointInline,InvestionResultPointInline,]

admin.site.register(Investion, InvestionAdmin)

class InvestionOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in InvestionOrder._meta.fields]
admin.site.register(InvestionOrder, InvestionOrderAdmin)

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

class StatusInvestionOrderAdmin(admin.ModelAdmin):
	list_display = [field.name for field in StatusInvestionOrder._meta.fields]
admin.site.register(StatusInvestionOrder, StatusInvestionOrderAdmin)
