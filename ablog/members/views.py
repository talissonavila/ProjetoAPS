
from django.contrib.auth.views import PasswordChangeView
from django.db.models.base import Model as Model
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from theblog.models import Profile

from .forms import (EditProfileForm, PasswordChangingForm, ProfilePageForm,
                    SignUpForm)


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    #tentar mudar pro home
    # success_url = reverse_lazy("home")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy("password_success")


class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = "registration/edit_profile_page.html"
    fields = ['bio', 'profile_picture', 'website_url', 'github_url', 'linkedin_url', 'instagram_url']
    success_url = reverse_lazy("home")


class CreateProfilePageView(generic.CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def password_success(request):
    return render(request, "registration/password_success.html", {})
