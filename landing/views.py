from django.shortcuts import render
from products.models import *


def landing(request):
    product_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    product_images_fresh = product_images.filter(product__category__id=2)
    product_images_freezy = product_images.filter(product__category__id=1)
    return render(request, 'landing/landing.html', locals())
