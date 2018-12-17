from django.db import models

# Create your models here.
class ProductCategory(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = 'Категория продукции'
		verbose_name_plural = 'Категории продукции'


class Product(models.Model):
	name = models.CharField(max_length=64, blank=True, null=True, default=None)
	category = models.ForeignKey(ProductCategory, on_delete=models.SET_DEFAULT, max_length=64, blank=True, null=True, default=None)
	price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	description = models.TextField(blank=True, null=True, default=None)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)

	def __str__(self):
		return "%s" % self.name

	class Meta:
		verbose_name = 'Продукт'
		verbose_name_plural = 'Продукция'

class ProductImage(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
	image = models.ImageField(upload_to='product_images/')
	is_main = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True , auto_now=False)
	updated = models.DateTimeField(auto_now_add=False , auto_now=True)

	def __str__(self):
		return "%s" % self.image

	class Meta:
		verbose_name = 'Фотография продукции'
		verbose_name_plural = 'Фотографии продукции'
