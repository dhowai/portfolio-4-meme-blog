from django.contrib import admin
from .models import Post, Category, Comment, UserProfile
from mptt.admin import MPTTModelAdmin

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Comment, MPTTModelAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'category', 'posted_on')
    list_filter = ('posted_on', 'author')
    prepopulated_fields = {'slug': ('title',)}
