from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
]
