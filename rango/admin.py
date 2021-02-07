from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')
    
#show us the Page and Category in the admin login
admin.site.register(Category)
admin.site.register(Page, PageAdmin)
