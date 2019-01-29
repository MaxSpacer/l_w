# -*- coding: utf-8 -*-
# Django
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from datetime import datetime
# Project
from .forms import CallmecontactForm
from .models import Callmecontact
from bootstrap_modal_forms.mixins import PassRequestMixin, DeleteAjaxMixin


def landing(request):
    nowDate = datetime.now()
    return render(request, 'landing/landing.html', locals())

class CallmeCreateView(PassRequestMixin, SuccessMessageMixin,
                     generic.CreateView):
    template_name = 'landing/create_callme.html'
    form_class = CallmecontactForm
    success_message = 'Ваша заявка принята, вскоре мы вам перезвоним'
    success_url = reverse_lazy('landing')
