from django.views.generic import ListView
from django.urls import path
from .models import Team

urlpatterns = [
    # path('', views.index, name='landing'),
        # path('', ListView.as_view(queryset=Article.objects.all().order_by("-order_view"),template_name="landing/landing.html"))
    path('', ListView.as_view(queryset=Team.objects.filter(is_active=True).order_by("order_render"),template_name="aboutus/aboutus.html")),
]
