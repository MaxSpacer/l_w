"""coolbed_proj URL Configuration

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
from django.urls import re_path, path
from educations import views
app_name = 'educations'
urlpatterns = [
	path('<pk>/', views.education, name='education_n'),
    path('', views.education_list, name='educationlist_n'),
	path('create_eduorder/<pk>/', views.EduorderCreateView.as_view(), name='create_eduorder_n'),
	# path('create_eduorder/<int:education_id>/', views.EduorderCreateView.as_view(), name='create_eduorder_n'),

]
