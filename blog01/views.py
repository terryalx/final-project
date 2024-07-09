from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
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
from django import forms
from django.core.paginator import Paginator
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


def home(request):
    data_list = BlogPost.objects.all().order_by("-date")
    paginator = Paginator(data_list, 10)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "home.html", {"page_obj": page_obj})


class UserPostListView(ListView):
    model = BlogPost
    template_name = "user_posts.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return BlogPost.objects.filter(author=user).order_by("-date")


class PostDetailView(DetailView):
    model = BlogPost
    template_name = "post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = "post_form.html"
    fields = ["title", "post", "image", "tag"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["post"].widget = forms.Textarea(attrs={"rows": 10, "cols": 80})
        form.fields["post"].initial = ""
        form.fields["post"].label = "Post Content"
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user-posts', kwargs={"username": self.object.author})


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BlogPost
    template_name = "post_form.html"
    fields = ["title", "post"]

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["post"].widget = forms.Textarea(attrs={"rows": 10, "cols": 80})
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse("post-detail", kwargs={"pk": self.object.pk})


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = BlogPost
#     template_name = "user_posts.html"
#     success_url = "/"

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


@login_required
def post_delete(request, pk):
    post = get_object_or_404(BlogPost, id=pk)
    
    if post.author != request.user:
        return HttpResponseForbidden()

    if request.method == 'POST':
        post.delete()
        return redirect('user-posts', username=post.author.username)

    return redirect('user-posts', username=post.author.username)
