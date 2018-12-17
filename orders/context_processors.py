from django.template.context_processors import request
from .models import ProductinBasket
from products.models import *


def getting_basket_info(request):

    session_key = request.session.session_key
    if not session_key:
        #workaround for newer Django versions
        # request.session["session_key"] = 123
        # #re-apply value
        request.session.cycle_key()

    products_in_basket = ProductinBasket.objects.filter(pb_session_key=session_key, pb_is_active=True)
    products_total_nmb = products_in_basket.count()
    total_price = 0
    for product_in_basket in products_in_basket:
        total_price += product_in_basket.pb_total_price
    
    return locals()
