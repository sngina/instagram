from django.contrib import admin
from .models import Image , Comment, Profile

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name' , 'post' , 'body')
    actions = [ 'allow_comments']

    def allow_comments(self , request , queryset):
        queryset.update(active= True)

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('image' ,)

admin.site.register(Image)
admin.site.register(Profile)
admin.site.register(Comment)