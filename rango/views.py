from django.shortcuts import render, redirect
from django.http import HttpResponse
#importing category model
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm
from django.urls import reverse

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    #page needs to have a category
    if category is None:
        return redirect('/rango/')
        
    form = PageForm()
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()
            return redirect(reverse('rango:show_category',
                            kwargs={'category_name_slug':
                                    category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context=context_dict)

def add_category(request):
    form = CategoryForm()
    #http post
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        #it the form is valid
        if form.is_valid():
        #save category and return user back to the default index view
            form.save(commit=True)
            return redirect('/rango/')
        else:
            #print errors that occured
            print(form.errors)
    #render the form
    return render(request, 'rango/add_category.html', {'form': form})

def show_category(request, category_name_slug):
    #creates a dict that can later be used to pass on stuff
    context_dict = {}
    try:
        #tries to get a category and pages associated according to the slug
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        #adds findings to the dictionary
        context_dict['pages'] = pages
        context_dict['category'] = category
        #or throws an exeption
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    #renders a response for the client with the dict required    
    return render(request, 'rango/category.html', context=context_dict)

#creates a view about
def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Romana Canigova'}
    #renders a response for the client with the dict required
    return render(request, 'rango/about.html', context=context_dict)
#creates a view index
def index(request):
    #takes the 5 most liked categories as a list
    context_dict = {}
    #a dictionary to match the variables in templates
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5] 
    #populating the dictionary 
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    #renders a response for the client with the dict required
    return render(request, 'rango/index.html', context=context_dict)