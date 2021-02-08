from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    #creates a path to the view about
    path('about/', views.about, name='about'),
    #path to any category according to its slug
    path('category/<slug:category_name_slug>/',
        views.show_category, name='show_category'),]