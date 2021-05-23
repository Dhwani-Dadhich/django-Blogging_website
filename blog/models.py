from django.db import models
from django.db.models.deletion import CASCADE
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from ckeditor_uploader.utils import slugify_filename

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=255)
    cat_pic = models.ImageField(upload_to = "images//", null=True)
    
    def __str__(self):                                #object ne string ma convert krva mate eg notice(1) = hie
        return self.category_name
   
   
   
class NewsletterUser(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    def __str__(self):
        return self.email
   
   

   
   
    
class Blog(models.Model):
    subject = models.CharField(max_length=400)
    slug = models.SlugField(null=True, blank=True)
    content = RichTextUploadingField(blank=True, null=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to = "images//", null=True)
    category_name = models.CharField(max_length=100, blank=True, null=True)
    
   #foreign key used when one to many relation...like ek branch ke bohot sare notice ho skte he and branch wale class se iska table banega isliye foriegn key use ki
    def __str__(self):                                #object ne string ma convert krva mate eg notice(1) = hie
        return self.subject
    
    def save(self, *args, **kwargs):
        self.slug = slugify_filename(self.subject)
        super(Blog, self).save(*args, **kwargs)
        

    
class Comment(models.Model):
    post = models.ForeignKey(Blog, related_name="comments", on_delete=CASCADE, null=True, blank=True)
    name =  models.CharField(max_length=400, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    reply = models.ForeignKey('Comment', on_delete=CASCADE, null=True, blank=True, related_name="replies")
    
    def __str__(self):
        return self.name
    
    
    
class Contact(models.Model):
    first = models.CharField(max_length=300, null=True, blank=True)
    last = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField(unique=True,null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    
    