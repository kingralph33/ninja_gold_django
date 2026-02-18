from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^process_money/$', views.process_money),
    re_path(r'^reset/$', views.reset),
]