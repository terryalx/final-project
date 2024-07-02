from django.shortcuts import render
from . models import BlogPost, BookStore

def home(request):
    data = BlogPost.objects.all()
    return render(request, 'home.html', {'data': data})

def books(request):
    data = BookStore.objects.all()
    return render(request, 'books.html', {'data' : data})
