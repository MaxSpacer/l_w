from django.contrib import admin
from .models import Bill, MemberPreference


class MemberPreferenceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MemberPreference._meta.fields]
admin.site.register(MemberPreference, MemberPreferenceAdmin)

class BillAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Bill._meta.fields]
admin.site.register(Bill, BillAdmin)
