from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import BlogPost


def home(request):
    context = {"posts": BlogPost.objects.all()}
    return render(request, "home.html", context)


class PostListView(ListView):
    model = BlogPost
    template_name = "home.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    ordering = ["-date"]
    paginate_by = 5


class UserPostListView(ListView):
    model = BlogPost
    template_name = "user_posts.html"  # <app>/<model>_<viewtype>.html
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return BlogPost.objects.filter(author=user).order_by("-date")


class PostDetailView(DetailView):
    model = BlogPost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    fields = ["title", "post"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    fields = ["title", "post"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BlogPost
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, "about.html", {"title": "About"})
