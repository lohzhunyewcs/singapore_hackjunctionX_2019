from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("api/process/", views.process_image),
    path("choose_items/", views.chooseItem),
    path("api/makechoice/", views.makechoice)
] 