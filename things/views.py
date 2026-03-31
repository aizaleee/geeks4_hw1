from django.shortcuts import render
from django.http import HttpResponse

def flower(request):
    return HttpResponse('welcome to your flower web')

def main(request):

    return render(request, "base.html")

def about(request):

    return HttpResponse("<h1>About us</h1> <a href='/'>Main</a>")