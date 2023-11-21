from django.urls import path

from . import views

urlpatterns = [
    path("index1", views.index, name="index"),
    path("index2", views.index_2, name="index_2"),
]