from django.db import models
from django.db.models.signals import post_save
from products.models import Product
from deployutils.main import disable_for_loaddata

class Status_order(models.Model):
    status_name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.status_name
    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'

# Create your models here.
class Order(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(max_length=64, blank=True, null=True, default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    customer_adress = models.CharField(max_length=128, blank=True, null=True, default=None)
    customer_comments = models.TextField(blank=True, null=True, default=None)
    total_price_order = models.DecimalField(max_digits=10, decimal_places=2, default=0) #total_price in order for all products
    status = models.ForeignKey(Status_order, on_delete=models.SET_DEFAULT, default=1)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "Заказ № %s %s" % (self.id, self.status.status_name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

class ProductinOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    qty = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*qty
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True , auto_now=False)
    updated = models.DateTimeField(auto_now_add=False , auto_now=True)

    def __str__(self):
        return "%s" % self.product

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.qty * self.price_per_item
        super(ProductinOrder, self).save(*args, **kwargs)

@disable_for_loaddata
def product_in_order_post_save(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductinOrder.objects.filter(order=order, is_active=True)
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price
    instance.order.total_price_order = order_total_price
    instance.order.save(force_update=True)

post_save.connect(product_in_order_post_save, sender=ProductinOrder)

class ProductinBasket(models.Model):
    pb_session_key = models.CharField(max_length=128, default=None)
    pb_order = models.ForeignKey(Order, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    pb_product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, blank=True, null=True, default=None)
    pb_qty = models.IntegerField(default=1)
    pb_price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    pb_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0) #price*qty
    pb_is_active = models.BooleanField(default=True)
    pb_created = models.DateTimeField(auto_now_add=True , auto_now=False)
    pb_updated = models.DateTimeField(auto_now_add=False , auto_now=True)


    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return "%s" % self.pb_product

    def save(self, *args, **kwargs):
        price_per_item = self.pb_product.price
        self.pb_price_per_item = price_per_item
        self.pb_total_price = int(self.pb_qty) * self.pb_price_per_item
        super(ProductinBasket, self).save(*args, **kwargs)
