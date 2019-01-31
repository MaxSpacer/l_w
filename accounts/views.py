# Django
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
from bootstrap_modal_forms.mixins import PassRequestMixin, LoginAjaxMixin
# Project
from .forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(PassRequestMixin, SuccessMessageMixin, generic.CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/signup.html'
    success_message = 'Success: Sign up succeeded. You can now <i class="fas fa-info fa-lg login-btn btn btn-dark p-1" type="button" name="button">login</i>.'
    success_url = reverse_lazy('landing')


class CustomLoginView(LoginAjaxMixin, SuccessMessageMixin, LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'accounts/login.html'
    success_message = 'Success: You were successfully logged in.'
    success_url = reverse_lazy('landing')
