

"""Definition of forms."""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm

from finder_api.models import Reviews, User


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
        exclude = ["uuid","created_at", "user","restaurant"]
        widgets = {
            "rating": forms.Select(
                attrs={
                    "class": "custom-select",
                    "id": "rating-select",
                    "aria-label": "Rating select",
                },
                choices=[(x / 10, f"{x / 10:.1f}") for x in range(101)],
            ),
            "review_text": forms.Textarea(
                attrs={
                    "class": "custom-textarea",
                    "placeholder": "Write your review here...",
                    "rows": 3,
                }
            ),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add a common class for styling all fields
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = field.widget.attrs.get("class", "") + " custom-input"

        

class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                    required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                                'class': 'form-control',
                                                                }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                                'class': 'form-control',
                                                                }))
    username = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control',
                                                                }))
    email = forms.EmailField(required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                            'class': 'form-control',
                                                            }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                    'class': 'form-control',
                                                                    'data-toggle': 'password',
                                                                    'id': 'password',
                                                                    }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                    'class': 'form-control',
                                                                    'data-toggle': 'password',
                                                                    'id': 'password',
                                                                    }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

