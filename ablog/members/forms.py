from re import A
from typing import Any

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from theblog.models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs["class"] = "form-control"
        self.fields['password1'].widget.attrs["class"] = "form-control"
        self.fields['password2'].widget.attrs["class"] = "form-control"


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "type": "password"}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_picture', 'website_url', 'github_url', 'linkedin_url', 'instagram_url')
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Entry your profile bio.'}),
            #'profile_picture': forms.Textarea(attrs=),
            'website_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inform your website url.'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inform your github url.'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inform your linkedin url.'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inform your instagram url.'}),
        }
        