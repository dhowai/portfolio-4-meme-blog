from django.test import TestCase
from .models import Post, Category, Comment, UserProfile
from django.urls import reverse
from django.contrib.auth.models import User


class TestModels(TestCase):

    def test_post_string_method_returns_title(self):
        title = Post.objects.create(title='Test Title')
        self.assertEqual(str(title), 'Test Title')

    def test_category_string_method_returns_name(self):
        name = Category.objects.create(name='Test Category')
        self.assertEqual(str(name), 'Test Category')

    def test_userprofile_string_method_returns_user(self):
        user = User.objects.create_user(username='testuser', password='12345')
        self.assertEqual(str(user), 'testuser')

    def test_model_str(self):
        comment = Comment.objects.create(body='test body', name='test name')
        self.assertEqual(str(comment), "Comment test body by test name")
