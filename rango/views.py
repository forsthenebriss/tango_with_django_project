from django.shortcuts import render
from django.http import HttpResponse


#creates a view about
def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")

#creates a view index
def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about/'>About</a>")