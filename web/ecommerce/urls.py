from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index),
    path("api/process/", views.process_image),
    re_path(r'^charts/$', views.charts, name='charts')
] 