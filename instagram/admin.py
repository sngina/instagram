from django.contrib import admin
from .models import Image , Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'post' , 'body')

    def allow_comments(self , request , queryset):
        queryset.update(active= True)