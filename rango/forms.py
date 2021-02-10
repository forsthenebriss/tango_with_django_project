from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    #additional properties
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


#class allowing to create a form from a preexisting model
class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    #helps provide association within model and model form
    class Meta:
        model = Category
        fields = ('name',)
        
class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        #excluding the category field from the form
        #better bcs we want to exclude less than include, otherwise specify
        exclude = ('category',)
        
        #function to check whether the url has correct formatting and if not, appends it
        def clean(self):
            cleaned_data = self.cleaned_data
            url = cleaned_data.get('url')
            # prepend 'http://' if not already there
            if url and not url.startswith('http://'):
                url = f'http://{url}'
                cleaned_data['url'] = url
                return cleaned_data