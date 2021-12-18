from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .forms import RegisterForm, EditUserSettingsForm, PasswordChangingForm, ProfilePageForm, EditProfilePageForm
from memeblog.models import UserProfile


class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "Registered Succesfully"


class UserEditSettingsView(SuccessMessageMixin, generic.UpdateView):
    form_class = EditUserSettingsForm
    template_name = 'registration/edit_user_settings.html'
    success_url = reverse_lazy('home')
    success_message = "User Settings Updated"

    def get_object(self):
        return self.request.user


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
    success_message = "Password Succesfully Updated"


class ProfilePageView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
    model = UserProfile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    success_message = "Profile Succesfully Updated"


class CreateProfilePageView(SuccessMessageMixin, generic.CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    success_message = "Profile Succesfully Created, You can now make Posts!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
