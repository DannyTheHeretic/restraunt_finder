from django.urls import path
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.views.generic.base import TemplateView

from finder_api import views_class
from finder_api import views_renders

passwords = [
    path(
        "password-reset/",
        views_class.ResetPasswordView.as_view(),
        name="password_reset",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="app/password/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        PasswordResetCompleteView.as_view(
            template_name="app/password/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
    path("register", views_class.RegisterView.as_view(), name="register"),
]


urlpatterns = [
    path("", views_renders.index, name="index"),
    path("about", views_renders.about, name="about"),
    # Cuisine
    path("cuisine/<str:catagory>", views_renders.cuisine, name="cuisine"),
    path("cuisine", views_renders.all_cuisine, name="cuisine"),
    path("restaurant/<str:name>", views_renders.restaurant, name="restaurant"),
    path("search", views_renders.search, name="search"),
    path("account", views_renders.account, name="account"),
    path("accounts/<str:uuid>", views_renders.other_users, name="accounts"),
    path("privacy", views_renders.privacy, name="privacy"),
    path("terms-of-service", views_renders.tos, name="tos"),
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    
    *passwords,
]
