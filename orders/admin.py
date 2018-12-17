from django.contrib import admin
from orders.models import *
# Register your models here.
#admin.site.register(Article)

class ProductinOrderInline(admin.TabularInline):
	model = ProductinOrder
	extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductinOrderInline]

admin.site.register(Order, OrderAdmin)

class Status_orderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status_order._meta.fields]
admin.site.register(Status_order, Status_orderAdmin)

class ProductinOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductinOrder._meta.fields]
admin.site.register(ProductinOrder, ProductinOrderAdmin)

class ProductinBasketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductinBasket._meta.fields]
admin.site.register(ProductinBasket, ProductinBasketAdmin)
