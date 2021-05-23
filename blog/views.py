from django.views.generic.list import ListView
from blog.models import Blog, Category, Comment, Contact
from django.views.generic.detail import DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView, DeleteView,\
    FormView, FormMixin
from dataclasses import fields
from django.views.generic.base import TemplateView
from django.http.response import HttpResponseRedirect, JsonResponse
from pip._vendor.requests.api import post
from rest_framework import viewsets
from django.contrib.auth.models import User
from blog.models import Blog, NewsletterUser, Contact
from blog import views
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from techfluenzer import settings
from blog import forms
from .forms import NewsletterUserSignUpForm

from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template, render_to_string
# Create your views here.
from .models import NewsletterUser
from .forms import NewsletterUserSignUpForm
from django.contrib import messages
from techfluenzer import settings
from django.template.response import TemplateResponse
from blog.forms import ContactForm, PopupSignUpForm, CommentForm


# Create your views here.


class HomeView(TemplateView, FormMixin):
    
    model = Blog
    template_name = "blog/blog_list.html"
    ordering = ['id']
    form_class = NewsletterUserSignUpForm
    
    def newsletter_sign_up(self, request):
        form = NewsletterUserSignUpForm(request.POST or None)
    
        if form.is_valid():
            instance = form.save(commit=False)
        
    
            if NewsletterUser.objects.filter(email=instance.email).exists():

                messages.warning(request,
                             "Your Email is already registered", 
                             "alert alert-warning alert-dismissible")
            
                subject = "Thank You For Joining Techfluenzer"
                from_email = settings.EMAIL_HOST_USER
                to_email = [instance.email]
                with open(settings.BASE_DIR + "/blog/templates/blog/signup_email.txt") as f:
                    signup_message = f.read()
                    message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
                    html_template = get_template("blog/signup_email.html").render()
                    message.attach_alternative(html_template, "text/html")
                    message.send()
        
            else:
                instance.save()
                messages.success(request,
                             "Your Email is successfully registered", 
                             "alert alert-success alert-dismissible")
        
        
        
        
        
        context = {
        'form': form,
        }
        template = "blog/sign_up.html"
        return render(request, template, context)

    
    

def home(request):
    if request.method == 'POST':
        form = NewsletterUserSignUpForm(request.POST)
    
        if form.is_valid():
            
            instance = form.save(commit=False)
        
    
            if NewsletterUser.objects.filter(email=instance.email).exists():

                messages.warning(request,
                             "Your Email is already registered", 
                             "alert alert-warning alert-dismissible")
            
                subject = "Thank You For Joining Techfluenzer"
                from_email = settings.EMAIL_HOST_USER
                to_email = [instance.email]
                with open(settings.BASE_DIR + "/blog/templates/blog/signup_email.txt") as f:
                    signup_message = f.read()
                message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
                html_template = get_template("blog/signup_email.html").render()
                message.attach_alternative(html_template, "text/html")
                message.send()
        
            else:
                instance.save()
                messages.success(request,
                             "Your Email is successfully registered", 
                             "alert alert-success alert-dismissible")
        
        
        
        
        
        
        
        context = {
        'form': form,
        }
        template = "blog/blog_list.html"
        return render(request, template, context)

    





    
    #def get_context_data(self,*args, **kwargs):
        
        #cat_menu = Category.objects.all()
        #context = super(HomeView, self).get_context_data(*args, **kwargs)
        #context["cat_menu"] = cat_menu
        #return context
        
#class CategoryListView(ListView):
#    model = Category
#    template_name = 'blog/category_list.html'
    
    
class CategoryListView(ListView):
    model = Category
    context_object_name = 'obj'
    
    
#def OR
    #cat_menu_list = Category.objects.all()
    #return HttpResponseRedirect(redirect_to="category_list")
    

   
        


class About(TemplateView):
    
    model = Blog
    template_name = "blog/about.html"
    
    
class Sitemap(TemplateView):
    
    model = Blog
    template_name = "blog/sitemap.html"



def ContactView(request):
    form = ContactForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('../blog/list')
        subject = "Thank You For Joining Techfluenzer"
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]
        with open(settings.BASE_DIR + "/blog/templates/blog/contact_email.txt") as f:
            signup_message = f.read()
        message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
        html_template = get_template("blog/contact_email.html").render()
        message.attach_alternative(html_template, "text/html")
        message.send()
    context = {
        'form': form,
        }
    template = "blog/contact.html"
    return render(request, template, context)






def CommentView(request,pk, slug):
    form = CommentForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        subject = "Thank You For Joining Techfluenzer"
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.email]
        with open(settings.BASE_DIR + "/blog/templates/blog/contact_email.txt") as f:
            signup_message = f.read()
        message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
        html_template = get_template("blog/contact_email.html").render()
        message.attach_alternative(html_template, "text/html")
        message.send()
    context = {
        'form': form,
        }
    template = "blog/blog_detail.html"
    return render(request, template, context)











@method_decorator(login_required, name="dispatch") 
class BlogCreate(CreateView):
    model = Blog
    fields = ["subject", "content", "category_name", "pic"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.uploaded_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    
    
    
    
    
           
    




def newsletter_subscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        
    
        if NewsletterUser.objects.filter(email=instance.email).exists():

            messages.warning(request,
                             "Your Email is already registered", 
                             "alert alert-warning alert-dismissible")
            
            
        else:
            instance.save()
            messages.success(request,
                             "Your Email is successfully registered", 
                             "alert alert-success alert-dismissible ")
            
            subject = "Thank You For Joining Techfluenzer"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/blog/templates/blog/signup_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("blog/signup_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
        
        
        
        
        
        
        
    context = {
        'form': form,
        }
    template = "blog/blog_list.html"
    return render(request, template, context)
















def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            messages.success(request,
                             "Your Email has been successfully removed", 
                             "alert alert-success alert-dismissible")
            
            subject = "You have been unsubscribed fron Techfluenzer"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/blog/templates/blog/unsubscribe_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("blog/unsubscribe_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
            
            
        else:
            messages.warning(request,
                             "Your Email is not registered", 
                             "alert alert-warning alert-dismissible")
            
    context = {
        'form': form,
        }
    template = "blog/unsubscribe.html"
    return render(request, template, context)

class BlogListView(ListView):
    model = Blog
    

 #this will not allow this class view if the user is logged in
class BlogDetailView(DetailView):
    model = Blog
    ordering = ['cr_date']
    
        
        
def post_detail(request, pk, slug):
    post = get_object_or_404(Blog, pk=pk, slug=slug)
    comments = Comment.objects.filter(post=post, reply=None).order_by('-id')
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(pk=reply_id)
            comment = Comment.objects.create(post=post, email=request.email, content=content, reply=comment_qs)
            comment.save()
            
    else:
        comment_form = CommentForm()
        
    context = {
        'post' : post,
        'comments': comments,
        'comment_form': comment_form,
        }
    
    if request.is_ajax():
        html = render_to_string('blog/comment.html', context, request=request)
        return JsonResponse({'form': html})
        
    return render(request, 'blog/blog_detail.html', context)
        
        
        
        
        
        
        
        
        
        
        
        
def BlogDetail(request, pk, slug):
    blogs = Blog.objects.all()
    post = get_object_or_404(Blog, id=id, slug = slug)
    comments = post.comments.filter(post=post).order_by('-id')
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment = Comment.objects.create(post=post, email=request.email, content=content)
            comment.save()
        else:
            comment_form = CommentForm()
            
        context = {
            
            }
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.parent = parent_obj
            new_comment = comment_form.save(commit=False)
            new_comment.Post = post
            new_comment.save() 
            return redirect('blog/blog_detail.html', slug, {'blogs': blogs})
    else:
        comment_form = CommentForm()
    
    return render(request, 'blog/blog_detail.html', {'post': post})


 
 
 
 
 
 
 
    
    
    
             #this will not allow this class view if the user is logged in
class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/blog_delete.html"




class BlogUpdateView(UpdateView):
    model = Blog
    template_name = "blog/blog_update.html"
    fields = ["subject", "content", "pic", "category_name"]


#class AddCategoryView(CreateView ):
 #   model = Category
#    template_name = 'add_category.html'
 #   feilds = '__all__'
 
 
 
def CategoryView(request, cats):
    category_blog = Blog.objects.filter(category_name=cats.replace('-', ' ')).order_by('-cr_date')
    #return render(request, {'cats': cats.subject(), })
    return render(request, 'blog/categories.html', {'cats':cats.title().replace('-', ' '), 'category_blog': category_blog})
    

class AddCommentView(CreateView ):
    model = Comment
    template_name = 'add_comment.html'
    feilds = '__all__'

    
def popup(request):
    form = PopupSignUpForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.warning(request,
                             "Your Email already exists", 
                             "alert alert-warning alert-dismissible")
            
            
        else:
            instance.save()
            messages.success(request,
                             "Your Email has been successfully registered", 
                             "alert alert-success alert-dismissible")
            
            subject = "Thank You For Joining Techfluenzer"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            with open(settings.BASE_DIR + "/blog/templates/blog/popup_email.txt") as f:
                signup_message = f.read()
            message = EmailMultiAlternatives(subject=subject, body=signup_message, from_email=from_email, to=to_email)
            html_template = get_template("blog/popup_email.html").render()
            message.attach_alternative(html_template, "text/html")
            message.send()
    context = {
        'form': form,
        }
    template = "blog/subscribe.html"
    return render(request, template, context)




class Privacy(TemplateView):
    
    model = Blog
    template_name = "blog/privacy.html"




