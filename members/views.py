from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegisterForm, EditProfileForm, PasswordChangingForm, ProfilePageForm, EditProfilePageForm
from memeblog.models import UserProfile


class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserEditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')


class ProfilePageView(generic.DetailView):
    model = UserProfile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = UserProfile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')


class CreateProfilePageView(generic.CreateView):
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
