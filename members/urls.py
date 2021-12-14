from django.urls import path
from .views import UserRegisterView, UserEditSettingsView, PasswordsChangeView, ProfilePageView, EditProfilePageView, CreateProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_user_settings/', UserEditSettingsView.as_view(), name='edit_user_settings'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name="change_password"),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),
]
