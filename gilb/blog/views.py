from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import *
from .forms import *

# Create your views here.


class GetAllPosts(ListView):
    model = Post
    template_name = "blog/blog_index.html"
    context_object_name = "posts"
    paginate_by = 1


class PostsByCategories(ListView):
    model = Post
    template_name = "blog/blog_by_categories.html"
    context_object_name = "posts"
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = Category.objects.get(slug=self.kwargs["slug"])
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["slug"])


class GetPost(ListView):
    model = Post
    template_name = "blog/single_blog.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = CommentForm()

        comments = Comment.objects.filter(post__slug=self.kwargs["slug"])

        context['form'] = form
        context['comments'] = comments

        return context

    def get_queryset(self):
        return Post.objects.get(slug=self.kwargs["slug"])


def add_comment(request, slug):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.post = Post.objects.get(slug=slug)
            form.save()
            return redirect(Post.objects.get(slug=slug).get_absolute_url())
    else:
        form = CommentForm()
    return render(request, 'blog/single_blog.html', {'form': form})
