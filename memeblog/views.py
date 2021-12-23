from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.forms import model_to_dict
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import AddPostForm, EditPostForm, CommentForm


class HomeView(ListView):
    """
    A view that displays the homepage of the site.
    It gathers and displays all the posts made, the author,
    the category and the time posted. Posts are ordered by
    date posted and paginate by 6.
    """
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.order_by('-posted_on')
    paginate_by = 6


class PostDetailView(DetailView):
    """
    A view that displays a post on its own page.
    It gathers the data whether the post has
    any likes, comments and displays them along
    with the comment form.
    """
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()
        comments = post.comments
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        context['total_likes'] = total_likes
        context["liked"] = liked
        return context


class AddPostView(SuccessMessageMixin, CreateView):
    """
    A view that allows the user to add posts to the
    site. It uses the model Post, form AddPostform and
    displays it on the add_post.html template.
    All fields are required an when the successfully
    makes a post, a success message is displayed.
    """
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_message = """Your Post Called
        %(title)s Has Been Posted in %(category)s"""


class EditPostView(SuccessMessageMixin, UpdateView):
    """
    A view that allows the user to edit posts  made.
    It uses the model Post, form EditPostform and
    displays it on the edit_post.html template.
    User can change the title name, category and
    the image used. When a change is made a success
    message is displayed.
    """
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'
    success_message = """Your Post Called %(title)s
        Has Been Updated in %(category)s"""


class DeletePostView(SuccessMessageMixin, DeleteView):
    """
    A view that allows the user to delete a post only
    if they created it. It uses the model Post and
    displays it on the delete_post.html template.
    """
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    success_message = "Your Post Called %(title)s Has Been Deleted"

    def delete_form_valid(self, object):
        """
        A success message cannot be used for the DeleteView. Therefore
        this function taken from the django documents is used to
        display the success message of the DeleteView.
        """
        success_message = self.get_success_message(model_to_dict(object))
        if success_message:
            messages.success(self.request, success_message)

    def delete(self, *args, **kwargs):
        object = self.get_object()
        result = super().delete(*args, **kwargs)
        self.delete_form_valid(object)
        return result


class CategoryView(ListView):
    """
    A view that displays all the posts with the same category
    on their own page.
    """
    template_name = 'category_page.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        context = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category=self.kwargs['category'])
        }
        return context


def category_list(request):
    """
    A view that displays all the categories in the nav bar.
    Once clicked a user is taken to the categoryview for that category.
    This can be accessed anywhere on the site.
    """
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return context


def like_view(request, pk):
    """
    A view that allows the user to like posts.
    The user can only like a post once, once liked they
    then only have the option to unlike. The user gets
    redirected to the same page when liking/unliking a post.
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


def comment_view(request, pk):
    """
    A view that handles the commenting section. A user fills the
    CommentForm, the form gathers the user's username, comment and
    saves it. The user is then redirected to the same page with
    their comment displayed below with their details.
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    comment_form = CommentForm(data=request.POST)
    if comment_form.is_valid():
        comment_form.instance.name = request.user.username
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
    else:
        comment_form = CommentForm()

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
