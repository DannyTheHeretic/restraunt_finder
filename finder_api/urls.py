from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cuisine/<str:catagory>", views.cuisine, name="cuisine"),
    
]
