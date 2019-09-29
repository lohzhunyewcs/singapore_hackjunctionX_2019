from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index),
    path("api/process/", views.process_image),
    path("choose_items/", views.chooseItem),
    path("api/makechoice/", views.makechoice),
    re_path(r'^charts/$', views.charts, name='charts'),
] 