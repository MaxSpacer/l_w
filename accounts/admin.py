# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *
from educations.models import EducationOrder
from landing.models import Mainformcontact, Callmecontact
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User



# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profile'
#     readonly_fields = ('reflink','referals_qty',)

# # Define a new User admin
# class UserAdmin(BaseUserAdmin):
#     inlines = (ProfileInline,)
#     # inlines = (ProfileInline,)
#
# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
class MainformcontactInline(admin.TabularInline):
    model = Mainformcontact
    readonly_fields = [field.name for field in Mainformcontact._meta.fields]

class EducationOrderInline(admin.TabularInline):
    model = EducationOrder
    readonly_fields = [field.name for field in EducationOrder._meta.fields]

class CallmecontactInline(admin.TabularInline):
    model = Callmecontact
    readonly_fields = [field.name for field in Callmecontact._meta.fields]

class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_display_links = ('user','id')
    readonly_fields = ('user','reflink','referals_qty')
    inlines = [EducationOrderInline,MainformcontactInline,CallmecontactInline,]
    # inlines = [MainformcontactInline]
admin.site.register(Profile, ProfileAdmin)
