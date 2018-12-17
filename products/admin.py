from django.contrib import admin
from products.models import *
# Register your models here.
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]
admin.site.register(ProductCategory, ProductCategoryAdmin)

class ProductImageInline(admin.TabularInline):
	model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
admin.site.register(Product, ProductAdmin)

class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]
admin.site.register(ProductImage, ProductImageAdmin)
