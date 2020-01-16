from django.shortcuts import render
from django.http import HttpResponse # How to handle certain routes

# Create your views here.


def home(request):
    return HttpResponse('<h1>blog home</h1>')


def about(request):
    return HttpResponse('<h1> bloh About</h1>')
