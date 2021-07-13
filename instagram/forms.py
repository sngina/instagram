from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from .models import Image, Profile , Comment
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User 
        fields = ('username' , 'first_name' ,'last_name', 'email' )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ('profile_photo' ,'bio' )

class   ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_name','image_photo' , 'image_caption')

class   CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body' ,)