from django.urls import path
from .views import HomeView, PostDetailView, AddPostView, EditPostView, DeletePostView, CategoryView, LikeView, CommentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', EditPostView.as_view(), name='edit_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<category>/', CategoryView.as_view(), name='category'),
    path('like/<int:pk>', LikeView, name="like_post"),
    path('comment/<int:pk>', CommentView, name="comment_post"),
]