from django.db import models
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.dispatch import receiver 
from django.db.models.signals import post_save

# Create your models here.
class Image(models.Model):
    image_photo = models.ImageField(upload_to = 'image/' , null = True)
    image_name = models.CharField(max_length=30)
    image_caption = models.CharField(max_length=30)

    # the save function
    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()
    #delete function for image
    @classmethod
    def delete_image(cls ,id):
        cls.objects.filter(id = id).delete()
    
    #updating caption
    @classmethod
    def update(cls , id , update) :
        caption = cls.objects.filter(id = id).update(image_caption = update)

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete= models.CASCADE , null = True)
    profile_photo = models.CharField(max_length= 30)
    bio = models.CharField(max_length= 30)

    #search for profile
    @receiver(post_save , sender = User)
    def create_profile(sender , instance , created , **kwargs):
        if created:
            Profile.objects.create(user = instance)
    @receiver(post_save , sender = User)
    def save_profile(sender , instance  , **kwargs):
        instance.profile.save()

    @classmethod 
    def search_profile(cls , profile ):
        name = cls.objects.filter(profile_image = profile)

class Comment(models.Model):
    post= models.ForeignKey(Image ,on_delete=models.CASCADE , related_name= 'comments')
    body = models.TextField()
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return 'Comment {} by {}'.format(self.body , self.name)