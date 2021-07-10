from django.core.checks import messages
from django.shortcuts import render , redirect
from django.http import HttpResponse ,Http404 
from .models import Image, Profile

# returning images 
def get_image(request):
    all_images = Image.objects.all()
    return render(request , 'profile/index.html', {"all_images" : all_images})

# function for searching users
def search(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        search_profile = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request , 'profile/search.html' ,{"message" : message , "search_profile":search_profile} ) 

    else:
        message = "You haven't searched for any profile"
        return render(request , 'profile/search.html')