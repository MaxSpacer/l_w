from django.contrib import admin
from events.models import *


class EventCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventCategory._meta.fields]
admin.site.register(EventCategory, EventCategoryAdmin)


class EventFormatAdmin(admin.ModelAdmin):
    list_display = [field.name for field in EventFormat._meta.fields]
admin.site.register(EventFormat, EventFormatAdmin)


class EventImageInline(admin.TabularInline):
    model = EventImage

# class EventResultPointInline(admin.TabularInline):
#     model = EventResultPoint
#
#
# class EventPlanPointInline(admin.TabularInline):
#     model = EventPlanPoint


class EventAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Event._meta.fields]
    list_display_links = ('name','id')
    inlines = [EventImageInline]
    # inlines = [EventPlanPointInline]
    # inlines = [EventResultPointInline]
admin.site.register(Event, EventAdmin)


class EventJoinerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in EventJoiner._meta.fields]
admin.site.register(EventJoiner, EventJoinerAdmin)


class StatusEventJoinerAdmin(admin.ModelAdmin):
	list_display = [field.name for field in StatusEventJoiner._meta.fields]
admin.site.register(StatusEventJoiner, StatusEventJoinerAdmin)
