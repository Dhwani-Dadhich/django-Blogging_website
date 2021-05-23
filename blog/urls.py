"""techfluenzer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from blog import views
from django.contrib.messages.api import success
from django.views.generic.base import RedirectView
from blog.views import CategoryListView
from blog.forms import CategoryForm


urlpatterns = [
    
    path('', RedirectView.as_view(url="blog/list")),
    path('blog/contact_us', views.ContactView),
     path('blog/about_us', views.About.as_view()),
     path('blog/privacy', views.Privacy.as_view()),
     path('blog/create/', views.BlogCreate.as_view(success_url = "/blog/blog/list")),
     path('blog/detail/<int:pk>/<slug:slug>', views.post_detail),
     path('blog/list', views.newsletter_subscribe, name='home'),
     path('blog/delete/<int:pk>', views.BlogDeleteView.as_view(success_url="/blog/blog/list")),
     path('blog/edit/<int:pk>', views.BlogUpdateView.as_view(success_url="blog/blog/list")),
     path('<str:cats>/', views.CategoryView),
     path('blog/category_list', CategoryListView.as_view()),
     path('blog/detail/<int:pk>/comment/', views.AddCommentView.as_view(success_url = "/blog/blog/detail/<int:pk>")),
     path('sign_up/', views.newsletter_subscribe),
    path('unsubscribe/', views.newsletter_unsubscribe),
    path('blog/sitemap', views.Sitemap.as_view()),
    path('blog/popup', views.popup),
    path('blog/subscribe', views.newsletter_subscribe),
    
     ]


