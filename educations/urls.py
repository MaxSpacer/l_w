from django.urls import re_path, path
from educations import views
app_name = 'educations'
urlpatterns = [
	path('detail/<pk>/', views.education, name='education_n'),
    path('', views.education_list, name='educationlist_n'),
	path('create_eduorder/<pk>/', views.EduorderCreateView.as_view(), name='create_eduorder_n'),
	# path('create_eduorder/<int:education_id>/', views.EduorderCreateView.as_view(), name='create_eduorder_n'),

]
