""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import ListView
from django.urls import path
from modposting.models import Modpost

urlpatterns = [
    # path('', views.index, name='landing'),
        # path('', ListView.as_view(queryset=Article.objects.all().order_by("-order_view"),template_name="landing/landing.html"))
    path('', ListView.as_view(queryset=Modpost.objects.filter(is_active=True).order_by("order_render"),template_name="modposting/modposting.html")),
]
