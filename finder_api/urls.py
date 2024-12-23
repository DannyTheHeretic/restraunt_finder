from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("cuisine/<str:catagory>", views.cuisine, name="cuisine"),
    path("restaurant/<str:name>", views.restaurant, name="restaurant"),
    
    
]
