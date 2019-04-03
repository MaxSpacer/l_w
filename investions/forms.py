
from django import forms
from .models import InvestionOrder
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
# from django.forms import HiddenInput

class InvestionOrderForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = InvestionOrder
        fields = ['customer_name', 'customer_email','customer_phone']
