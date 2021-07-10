from django.core.checks import messages
from django.shortcuts import render , redirect
from django.http import HttpResponse ,Http404 
from .models import Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import UserForm , ProfileForm
# returning images 

@login_required(login_url= '/accounts/login/')
def get_image(request):
    all_images = Image.objects.all()
    return render(request , 'profile/index.html', {"all_images" : all_images})

def userpage(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request,"user.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })
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