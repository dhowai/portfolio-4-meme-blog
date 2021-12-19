from django import forms
from .models import Post, Category, Comment
from mptt.forms import TreeNodeChoiceField

categories = Category.objects.all().values_list('name', 'name')

categories_list = []

for item in categories:
    categories_list.append(item)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'author', 'content_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            'content_image': forms.FileInput(attrs={'class': 'form-control', 'required': True}),
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'content_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories_list, attrs={'class': 'form-control'}),
            'content_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''
        }

        widgets = {
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Your Comment Here'}),
        }
