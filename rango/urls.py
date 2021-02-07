from django.urls import path
from rango import views

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='index'),
    #creates a path to the view about
    path('about/', views.about, name='about'),
]