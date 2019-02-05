
from django import forms
from .models import EducationOrder
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
# from django.forms import HiddenInput

class EducationOrderForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = EducationOrder
        fields = ['customer_name', 'customer_email','customer_phone']
