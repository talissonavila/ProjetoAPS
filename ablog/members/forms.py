from typing import Any

from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from theblog.models import Profile


class SignUpForm(UserCreationForm):
    """A form for signing up a new user.

    Attributes:
        email (forms.EmailField): The user's email address.
        first_name (forms.CharField): The user's first name.
        last_name (forms.CharField): The user's last name.

    Meta:
        model (User): The model that this form is associated with.
        fields (tuple): The fields that are included in the form.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initializes the SignUpForm instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["class"] = "form-control"

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        """Metadata for the SignUpForm class.

        Attributes:
            model (User): The model that this form is associated with.
            fields (tuple): The fields that are included in the form.
        """

        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")


class EditProfileForm(UserChangeForm):
    """A form for editing a user's profile.

    Attributes:
        email (forms.EmailField): The user's email address.
        first_name (forms.CharField): The user's first name.
        last_name (forms.CharField): The user's last name.
        username (forms.CharField): The user's username.

    Meta:
        model (User): The model that this form is associated with.
        fields (tuple): The fields that are included in the form.
    """

    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        """Metadata for the EditProfileForm class.

        Attributes:
            model (User): The model that this form is associated with.
            fields (tuple): The fields that are included in the form.
        """

        model = User
        fields = ("username", "first_name", "last_name", "email")


class PasswordChangingForm(PasswordChangeForm):
    """A form for changing a user's password.

    Attributes:
        old_password (forms.CharField): The user's current password.
        new_password1 (forms.CharField): The user's new password.
        new_password2 (forms.CharField): The user's new password (confirmation).

    Meta:
        model (User): The model that this form is associated with.
        fields (tuple): The fields that are included in the form.
    """

    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}))

    class Meta:
        """Metadata for the PasswordChangingForm class.

        Attributes:
            model (User): The model that this form is associated with.
            fields (tuple): The fields that are included in the form.
        """

        model = User
        fields = ("old_password", "new_password1", "new_password2")


class ProfilePageForm(forms.ModelForm):
    """A form for editing a user's profile page.

    Meta:
        model (Profile): The model that this form is associated with.
        fields (tuple): The fields that are included in the form.
        widgets (dict): A dictionary of widgets to use for each field.
    """

    class Meta:
        """Metadata for the PasswordChangingForm class."""

        model = Profile
        fields = ("bio", "profile_picture", "website_url", "github_url", "linkedin_url", "instagram_url")
        widgets = {
            "bio": forms.Textarea(attrs={"class": "form-control", "placeholder": "Entry your profile bio."}),
            #'profile_picture': forms.Textarea(attrs=),
            "website_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "Inform your website url."}),
            "github_url": forms.TextInput(attrs={"class": "form-control", "placeholder": "Inform your github url."}),
            "linkedin_url": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Inform your linkedin url."}
            ),
            "instagram_url": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Inform your instagram url."}
            ),
        }
