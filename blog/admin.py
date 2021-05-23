from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from blog.models import Category, Blog, Comment, Contact


# Register your models here.
class BlogAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject"]
    list_filter = ["cr_date"]
    
#admin.site.register(models.Notice)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Contact)


# Register your models here.
from .models import NewsletterUser


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added')
    
    
admin.site.register(NewsletterUser, NewsletterAdmin)


class BlogCreate(admin.ModelAdmin):
    list_display = '__all__'
    search_fields = ["subject"]
    
    def form_valid(self, form):
        self.object = form.save()
        self.object.save()
    
