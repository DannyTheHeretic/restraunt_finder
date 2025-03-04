from django.urls import path, include
from django.views.generic.base import TemplateView

from finder_api import views


urlpatterns = [
    path("", views.index, name="index"),
    path("api/", include("finder_api.api.urls")),
    
    path("about", views.about, name="about"),
    # Cuisine
    path("cuisine/<str:catagory>", views.cuisine, name="cuisine"),
    path("cuisine", views.all_cuisine, name="cuisine"),
    path("restaurant/<str:name>", views.restaurant, name="restaurant"),
    path("search", views.search, name="search"),
    # Social Aspect
    path("account", views.account, name="account"),
    path("accounts/<str:uuid>", views.other_users, name="accounts"),
    path("accounts/<str:uuid>/followers", views.followers, name="followers"),
    path("privacy", views.privacy, name="privacy"),
    path("terms-of-service", views.tos, name="tos"),
    path("faceit-auth",views.faceit, name="code"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "ads.txt",
        TemplateView.as_view(template_name="ads.txt", content_type="text/plain"),
    ),
]
