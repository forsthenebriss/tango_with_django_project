import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                        'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page
import random
def populate():

    #creating lists of dictionaries with the data we want to add to each category
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/'},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/'},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/'}
                    ]
    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/'},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/'}
                   ]
    other_pages = [{'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/'},
        {'title':'Flask',
        'url':'http://flask.pocoo.org'}
                   ]

    # creating dictionary of dictionaries for the categories
    cats = {'Python': {'pages': python_pages, 'likes' : 64, 'views' : 128 },
            'Django': {'pages': django_pages,'likes' : 32, 'views' : 64 },
            'Other Frameworks': {'pages': other_pages,'likes' : 16, 'views' : 32 }
            }

    #go through the dictionary (cats) and adds the required pages
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['likes'], cat_data['views'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])
            
    #print out the added categories
    for c in Category.objects.all():         
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

#function top add a page into a category (if category does not exist, creates one)
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views= random.randrange(1000)
    p.save()
    return p

#function to add a category
def add_cat(name,likes=0, views=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c

#main execution start
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    
