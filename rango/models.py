from django.db import models

class Category(models.Model):
    #a name string of maximum 128 chars that must not already exist
    name = models.CharField(max_length=128, unique=True)
    #number of likes and views
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    
   #return name as string for easier manipulation
    def __str__(self):
        return self.name
    
    #changes the typo 'categorys' in plural to 'categories'
    class Meta:
        verbose_name_plural = 'Categories'
        
class Page(models.Model):
    #if deleted, everything connected deleted with the category
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #a title string of maximum 128 chars
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    
    #return name as string for easier manipulation
    def __str__(self):
        return self.title