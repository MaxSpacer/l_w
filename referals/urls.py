
from django.urls import re_path
from referals import views

urlpatterns = [
    re_path(r'^[-a-zA-Z0-9_]{4}(?P<referer_id>\d+)/$', views.ref_session_add, name='ref_session_add_n'),
]
