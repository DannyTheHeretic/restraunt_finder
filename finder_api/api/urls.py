from django.urls import path
from finder_api.api import endpoint

urlpatterns = [
    path("add_favorite", endpoint.add_to_favorites, name="add"),
    path("remove_favorite", endpoint.remove_to_favorites, name="remove"),
]
