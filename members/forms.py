from django.contrib.auth.forms import (
    UserCreationForm, UserChangeForm, PasswordChangeForm)
from django.contrib.auth.models import User
from django import forms
from memeblog.models import UserProfile


class RegisterForm(UserCreationForm):
    """
    This form handles the user registration extending from
    the UsercreationForm.
    """
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username', 'first_name',
            'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditUserDetailsForm(UserChangeForm):
    """
    This form handles the edit user setting extending from
    the UserChangeForm.
    """
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', )


class PasswordChangingForm(PasswordChangeForm):
    """
    This form handles the change of user password extending
    from the PassWordChangeForm.
    """
    old_password = forms.CharField(
        label="Old Password", max_length=100, widget=forms.PasswordInput(
            attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(
        label="New Password", max_length=100,  widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(
        label="Confirm Password", max_length=100, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2', )


class EditProfilePageForm(forms.ModelForm):
    """
    This form handles the edit user profile page
    information.
    """
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'bio')

        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ProfilePageForm(forms.ModelForm):
    """
    This form handles the user profile information
    page.
    """
    class Meta:
        model = UserProfile
        fields = ('profile_pic', 'bio')

        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }
