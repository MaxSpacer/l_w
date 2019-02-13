from django.contrib import admin
from events.models import *


# Register your models here.

class EventCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventCategory._meta.fields]
admin.site.register(EventCategory, EventCategoryAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]
    list_display_links = ('name','id')
admin.site.register(Event, EventAdmin)


class EventJoinerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in EventJoiner._meta.fields]
admin.site.register(EventJoiner, EventJoinerAdmin)

class StatusEventJoinerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in StatusEventJoiner._meta.fields]
admin.site.register(StatusEventJoiner, StatusEventJoinerAdmin)
