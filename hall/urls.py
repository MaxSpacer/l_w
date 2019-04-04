from . import views
from django.urls import path


app_name = 'hall'

urlpatterns = [
    path('', views.hall, name='hall_n'),
]
