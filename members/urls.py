from django.urls import path
from .views import UserRegisterView, UserEditProfileView, PasswordsChangeView, ProfilePageView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditProfileView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change_password.html'), name="change_password"),
    path('<int:pk>/profile/', ProfilePageView.as_view(), name='profile_page'),
]
