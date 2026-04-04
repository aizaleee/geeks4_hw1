from django.shortcuts import render
from django.http import HttpResponse
from things.models import Post

def flower(request):
    return HttpResponse('welcome to your flower web')

def main(request):

    return render(request, "base.html")

def about(request):

    return HttpResponse("<h1>About us</h1> <a href='/'>Main</a>")

def if_published(request):

    published = Post.objects.filter(is_published=True) 

    return render(request, "posts_view.html", context={"posts": published})