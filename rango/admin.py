from django.contrib import admin
from rango.models import Category, Page

#class that lists attributes in given order
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category', 'url')
    
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    
#show us the Page and Category in the admin login
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
