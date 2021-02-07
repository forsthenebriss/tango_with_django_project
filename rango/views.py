from django.shortcuts import render
from django.http import HttpResponse


#creates a view about
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Romana Canigova'}
    #renders a response for the client with the dict required
    return render(request, 'rango/about.html', context=context_dict)
#creates a view index
def index(request):
    # constructrs a dict to match the variables in the templates
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    #renders a response for the client with the dict required
    return render(request, 'rango/index.html', context=context_dict)