from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Record


class SignUpForm(UserCreationForm):
    """_summary_

    Args:
        UserCreationForm (_type_): _description_
    """

    email = forms.EmailField(
        max_length=254,
        help_text="Required. Inform a valid email address.",
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email address"}
        ),
    )

    first_name = forms.CharField(
        max_length=45,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First name"}
        ),
    )

    last_name = forms.CharField(
        max_length=45,
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last name"}
        ),
    )

    class Meta:
        """_summary_"""

        model: User = User
        fields: tuple = (
            "email",
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields["username"].max_length = 150
        self.fields["username"].help_text = (
            '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        )

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields["username"].max_length = 1000
        self.fields["password1"].help_text = (
            "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"
        )

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields["username"].max_length = 1000
        self.fields["password2"].help_text = (
            '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        )

# Add Record Form
class CreateRecordForm(forms.ModelForm):
    """_summary_

    Args:
        forms (_type_): _description_
    """

    first_name = forms.CharField(max_length=45, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "First name"}), required=True)
    last_name = forms.CharField(max_length=45, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Last name"}), required=True)
    email = forms.EmailField(max_length=254, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}), required=True)
    phone = forms.CharField(max_length=254, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Phone"}), required=True)
    address = forms.CharField(max_length=254, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Address"}), required=True)
    city = forms.CharField(max_length=254, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "City"}), required=True)
    state = forms.CharField(max_length=254, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "State"}), required=True)
    zipcode = forms.CharField(max_length=45, label="", widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Zipcode"}), required=True)

    class Meta:
        """_summary_"""
        model = Record
        fields = ('first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'zipcode')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        }
    # username = forms.CharField(
    #     max_length=45,
    #     label="",
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "User name"}
    #     ),
    # )

    # password1 = forms.CharField(
    #     max_length=1000,
    #     label="",
    #     widget=forms.PasswordInput(
    #         attrs={"class": "form-control", "placeholder": "Password"}
    #     ),
    # )

    # password2 = forms.CharField(
    #     max_length=1000,
    #     label="",
    #     widget=forms.PasswordInput(
    #         attrs={"class": "form-control", "placeholder": "Confirm password"}
    #     ),
    # )
