# Django
from django import forms
# Project
from .models import Callmecontact
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class CallmecontactForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Callmecontact
        fields = ['contact_name', 'contact_phone']
