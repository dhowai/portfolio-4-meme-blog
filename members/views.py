from django.shortcuts import get_object_or_404
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from memeblog.models import UserProfile
from .forms import (
    RegisterForm, EditUserDetailsForm,
    PasswordChangingForm, ProfilePageForm, EditProfilePageForm)


class UserRegisterView(SuccessMessageMixin, generic.CreateView):
    """
    User can register an account. The RegisterForm from forms gets
    passed through in the form_class. The form has the django
    validation, checking if the various fields are valid and
    prompts error messages appropritely. If successfull the
    user is then taken tp the login page with a succes message.
    """
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
    success_message = "%(username)s Registered Succesfully"


class EditUserDetailsView(SuccessMessageMixin, generic.UpdateView):
    """
    User can edit their information inputed initially in the register
    form. These details get pulled from the database and auto fill
    the fields with the intial information. Once the user clicks
    update the user is taken back to the home page and a success
    message gets displayed.
    """
    form_class = EditUserDetailsForm
    template_name = 'registration/edit_user_details.html'
    success_url = reverse_lazy('home')
    success_message = "User Settings Updated"

    def get_object(self):
        return self.request.user


class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    """
    User can change their password using this page. Once changed
    the user is taken back to the home page and a success
    message is displayed.
    """
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
    success_message = "Password Succesfully Updated"


class ProfilePageView(generic.DetailView):
    """
    The user can view their overall profile using this view.
    Also has links to the other pages to edit any information.
    """
    model = UserProfile
    template_name = (
        'registration/user_profile.html')

    def get_context_data(self, *args, **kwargs):
        context = super(ProfilePageView, self).get_context_data(
            *args, **kwargs)

        page_user = get_object_or_404(UserProfile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class EditProfilePageView(SuccessMessageMixin, generic.UpdateView):
    """
    The user can edit the profile image or bio information. When
    succesfull the user is redirected to the homepage and a success
    message is displayed.
    """
    model = UserProfile
    form_class = EditProfilePageForm
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    success_message = "Profile Succesfully Updated"


class CreateProfilePageView(SuccessMessageMixin, generic.CreateView):
    """
    Once the user initally registered and logs in for the first time
    they are given the option to create a profile page. The user
    would need to click on the link but not nessarly add any information
    in order to make posts. This finializes the user's information. On
    success the user then gets a success message displayed.
    """
    model = UserProfile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    success_message = "Profile Succesfully Created, You can now make Posts!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
