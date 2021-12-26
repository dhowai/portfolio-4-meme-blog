from django import forms
from .models import Post, Category, Comment

categories = Category.objects.all().values_list('name', 'name')

categories_list = []

for item in categories:
    categories_list.append(item)


class AddPostForm(forms.ModelForm):
    """
    Using this form the user can add a post to the site.
    The title needs to be unique, the categories are
    predetermined and the user can only choose what's
    in the list. The author field is hidden as the
    javascript gets the information of the user.
    The content image is the main part of the post
    and like all the other fields, it is required.
    """
    class Meta:
        """
        This uses the Post model and allows certain
        form fields to be manipulated and styled.
        """
        model = Post
        fields = ('title', 'category', 'author', 'content_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories_list, attrs={
                'class': 'form-control'}),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'value': '', 'id': 'user', 'type': 'hidden'}),
            'content_image': forms.FileInput(
                attrs={'class': 'form-control', 'required': True}),
        }


class EditPostForm(forms.ModelForm):
    """
    This form allows the user to edit their post
    made by changing the title, category or the image.
    This form has validation the in template which only
    allows the author to make edit this information.
    """
    class Meta:
        """
        This uses the Post model and allows certain
        form fields to be manipulated and styled.
        """
        model = Post
        fields = ('title', 'category', 'content_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=categories_list, attrs={
                'class': 'form-control'}),
            'content_image': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    """
    This form allows the user to make comments
    on a post's page.
    """
    class Meta:
        """
        This uses the Comment model and allows certain
        form fields to be manipulated and styled.
        """
        model = Comment
        fields = ('body',)
        labels = {
            'body': ''
        }

        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write Your Comment Here'}),
        }
