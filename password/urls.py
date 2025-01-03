from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path
from password import views

urlpatterns = [
    path(
        "password-reset/",
        views.ResetPasswordView.as_view(),
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
    path("register", views.RegisterView.as_view(), name="register"),
]
