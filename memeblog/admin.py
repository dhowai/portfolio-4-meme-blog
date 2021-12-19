from django.contrib import admin
from .models import Post, Category, Comment, UserProfile


admin.site.register(Category)
admin.site.register(UserProfile)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'category', 'posted_on')
    list_filter = ('posted_on', 'author')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'body', 'created_on')
    list_filter = ('created_on', 'name')
