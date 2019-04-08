

from django.urls import path
from . import views
from django.views.generic import ListView
from .models import Landpost
urlpatterns = [
    # path('', views.landing, name='landing'),
    path('create/', views.CallmeCreateView.as_view(), name='create_callme'),
    path('main_form/', views.MainFormView.as_view(), name='main_form'),
    path('', ListView.as_view(queryset=Landpost.objects.filter(is_active=True).order_by("order_render"),template_name="landing/landing.html"), name='main'),
]
