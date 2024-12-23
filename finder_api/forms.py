

"""Definition of forms."""

from datetime import UTC, datetime
import uuid
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _

from finder_api.models import Reviews


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""

    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput({"class": "form-control", "placeholder": "User name"}),
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(
            {"class": "form-control", "placeholder": "Password"},
        ),
    )
    

class ReviewsForm(forms.ModelForm):
    
    class Meta:
       model = Reviews
       exclude = ["created_by","pub_date","uuid", "anon_name","anon_email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

    