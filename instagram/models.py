from django.db import models
from django.shortcuts import render , redirect

# Create your models here.
class Image(models.Model):
    image_photo = models.ImageField(upload_to = 'image /' , null = True)
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
    profile_photo = models.CharField(max_length= 30)
    bio = models.CharField(max_length= 30)

    #function of getting all the images 
        