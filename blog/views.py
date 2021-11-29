from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import AddPostForm, EditPostForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    queryset = Post.objects.order_by('-posted_on')
    paginate_by = 6

    # Might remove
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        post_likes = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post_likes.total_likes()
        liked = False
        if post_likes.likes.filter(id=self.request.user.id).exists():
            liked = True
        context['total_likes'] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'


class EditPostView(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


class CategoryView(ListView):
    template_name = 'category_page.html'
    context_object_name = 'catlist'
    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category=self.kwargs['category'])
        }
        return content


def category_list(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list
    }
    return context


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
