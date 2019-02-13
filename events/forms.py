
from django import forms
from .models import EventJoiner
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
# from django.forms import HiddenInput

class EventJoinForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = EventJoiner
        fields = ['customer_name', 'customer_email','customer_phone']
