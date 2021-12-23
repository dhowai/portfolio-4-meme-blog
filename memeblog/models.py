from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Modal the handles the posts being made.
    """
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    posted_on = models.DateTimeField(auto_now=True)
    content_image = CloudinaryField('image')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    objects = models.Manager()

    class Meta:
        ordering = ['-posted_on']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('home')

    def total_likes(self):
        return self.likes


class Category(models.Model):
    """
    Modal that handles the category's of the site.
    """
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('home')


class Comment(models.Model):
    """
    Modal that handles the comment section.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class UserProfile(models.Model):
    """
    Modal that handles the user profile.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = CloudinaryField('image', default='default')
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('home')
