from django import forms
from .models import Blog, Category, NewsletterUser
from crispy_forms.helper import FormHelper
from blog.models import Contact, Comment


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['category_name']
        
        choices = Category.objects.all().values_list('category_name','category_name')
        
        choice_list=[]
        
        for item in choices:
            choice_list.append(item)
                
        widgets = {
            'category_name': forms.Select(choices=choice_list)
            }
        




class NewsletterUserSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True
    class Meta:
        model = NewsletterUser
        fields = ['name', 'email']
        name = forms.CharField(label="Name",
                                widget=forms.TextInput(attrs={'placeholder':'name'})) 
        email = forms.EmailField(label="Email", 
                                 widget=forms.EmailInput(attrs={'placeholder':'email'}))
        
        
        
        
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            
            return email





class PopupSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True
    class Meta:
        model = NewsletterUser
        fields = ['name', 'email']
        name = forms.CharField(label="Name",
                                widget=forms.TextInput(attrs={'placeholder':'name'})) 
        email = forms.EmailField(label="Email", 
                                 widget=forms.EmailInput(attrs={'placeholder':'email'}))
        
        
        
        
        
        def clean_email(self):
            email = self.cleaned_data.get('email')
            
            return email





        

class ContactForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True
    class Meta:
        model = Contact
        fields = ['first', 'last', 'email', 'comment']
        first = forms.CharField(label="First Name",
                                widget=forms.TextInput(attrs={'placeholder':'First Name'})) 
        
        last = forms.CharField(label="Last Name",
                                widget=forms.TextInput(attrs={'placeholder':'Last Name'}))
        
        email = forms.EmailField(label="Email", 
                                 widget=forms.EmailInput(attrs={'placeholder':'email'}))
        
        
        
        
        
        def clean_first(self):
            first = self.cleaned_data.get('first')
            
            return first

        def clean_last(self):
            last = self.cleaned_data.get('last')
            
            return last

        def clean_email(self):
            email = self.cleaned_data.get('email')
            
            return email

        def clean_comment(self):
            comment = self.cleaned_data.get('comment')
            
            return comment




class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment here', 'rows': 5, 'cols': 100}))
    class Meta:
        model = Comment
        fields = {'name', 'email', 'content'}
        
        
        
        
        
        
        
        
        
        