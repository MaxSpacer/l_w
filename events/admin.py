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

# class EventImageAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in EventImage._meta.fields]
# admin.site.register(EventImage, EventImageAdmin)
#
# class EventImageInline(admin.TabularInline):
#     model = EventImage
