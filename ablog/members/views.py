from django.contrib.auth.views import PasswordChangeView
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from theblog.models import Profile

from .forms import EditProfileForm, PasswordChangingForm, ProfilePageForm, SignUpForm


class UserRegisterView(generic.CreateView):
    """View for user registration.

    Attributes:
        form_class (SignUpForm): Form for user registration.
        template_name (str): Template for user registration.
        success_url (str): URL to redirect after successful registration.
    """

    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    """View for editing user profile.

    Attributes:
        form_class (EditProfileForm): Form for editing user profile.
        template_name (str): Template for editing user profile.
        success_url (str): URL to redirect after successful editing.
    """

    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self) -> object:
        """Returns user."""
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    """View for changing user password.

    Attributes:
        form_class (PasswordChangingForm): Form for changing user password.
        template_name (str): Template for changing user password.
        success_url (str): URL to redirect after successful password change.
    """

    form_class = PasswordChangingForm
    template_name = "registration/change-password.html"
    success_url = reverse_lazy("password_success")


class ShowProfilePageView(generic.DetailView):
    """View for displaying user profile.

    Attributes:
        model (Profile): Model for user profile.
        template_name (str): Template for displaying user profile.
    """

    model = Profile
    template_name = "registration/user_profile.html"

    def get_context_data(self, *args, **kwargs) -> dict:
        """Returns context data for displaying user profile."""
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs["pk"])
        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    """View for editing user profile page.

    Attributes:
        model (Profile): Model for user profile.
        template_name (str): Template for editing user profile page.
        fields (list): Fields to edit in user profile page.
        success_url (str): URL to redirect after successful editing.
    """

    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ["bio", "profile_picture", "website_url", "github_url", "linkedin_url", "instagram_url"]
    success_url = reverse_lazy("home")


class CreateProfilePageView(generic.CreateView):
    """View for creating user profile page.

    Attributes:
        model (Profile): Model for user profile.
        form_class (ProfilePageForm): Form for creating user profile page.
        template_name (str): Template for creating user profile page.
    """

    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form) -> object:
        """Returns valid form for creating user profile page."""
        form.instance.user = self.request.user
        return super().form_valid(form)


def password_success(request) -> object:
    """View for displaying password success message.

    Args:
        request (object): Request object.

    Returns:
        object: Rendered template.
    """
    return render(request, "registration/password_success.html", {})
