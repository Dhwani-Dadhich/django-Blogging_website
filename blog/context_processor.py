from .forms import NewsletterUserSignUpForm
from blog.models import Category, Blog, NewsletterUser
from blog.views import CategoryListView
from django.shortcuts import render
from builtins import all
from django.views.generic.list import ListView
from techfluenzer import settings
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.views.generic.detail import DetailView

def NewsletterSignUpFormGlobal(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    
    return {'form': form}



def CategoryGlobal(request):
    cat = Category.objects.all()
    return{"cat":cat}


def RecentGlobal(request):
    recent = Blog.objects.all().order_by('-cr_date')
    return{"recent":recent}


def CategoryViewGlobal(request):
    cat = Category.objects.all()
    category_blog = Blog.objects.filter(category_name=cat)
    return{'cat': cat, 'category_blog': category_blog}
   
   

    
