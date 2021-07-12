from django.core.checks import messages
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse ,Http404 
from .models import Comment, Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, UserForm , ProfileForm , ImageForm
# returning images 

@login_required(login_url= '/accounts/login/')
def get_image(request):
    all_images = Image.objects.all()
    if request.method == 'POST':
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            form = ImageForm()
    print(all_images)
    form = ImageForm()
    return render(request , 'profile/index.html',  {"all_images": all_images ,"imageform":form})
def success(request):
    return HttpResponse('successfully uploaded')
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

def p_detail(request) :
    if request.method == 'POST':
        comment_form = CommentForm(data= request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.save()

    else:
        comment_form = CommentForm()

    return render(request , "profile/comment.html" , 'comment_form' , comment_form)
# function  for returning image when clicked
def image_details(request , id):
    one_image = Image.objects.get(id = id)
    print(request)
    return render(request , 'profile/image.html' , {"one_image": one_image})

    