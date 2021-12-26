from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Post(models.Model):
    """
    Model the handles the posts being made.
    """
    title = models.CharField(max_length=200, unique=True)
    category = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    posted_on = models.DateTimeField(auto_now=True)
    content_image = CloudinaryField('image')
    likes = models.ManyToManyField(User, related_name='post_likes', blank=True)
    objects = models.Manager()

    class Meta:
        """
        Orders post by date/time, newest first.
        """
        ordering = ['-posted_on']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        """
        Redirects to home when posted
        """
        return reverse('home')

    def total_likes(self):
        """
        Returns post likes
        """
        return self.likes


class Category(models.Model):
    """
    Model that handles the category's of the site.
    """
    name = models.CharField(max_length=200)
    objects = models.Manager()

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    """
    Model that handles the comment section.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        """
        Orders comments by date/time, newest last.
        """
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class UserProfile(models.Model):
    """
    Model that handles the user profile.
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = CloudinaryField('image', default='default')
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        """
        Redirects to home when completed
        """
        return reverse('home')
