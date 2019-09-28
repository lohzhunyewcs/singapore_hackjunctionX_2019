from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("api/process/", views.process_image)
] 