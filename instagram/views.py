from django.core.checks import messages
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse ,Http404 
from .models import Comment, Image, Profile
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, UserForm , ProfileForm , ImageForm
from django.urls import reverse
# returning images 

@login_required(login_url= '/accounts/login/')
def get_image(request):
    all_images = Image.objects.all()
    comment = Comment.objects.all()
    print(comment)
    if request.method == 'POST':
        form = ImageForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
    c_form = CommentForm()
    form = ImageForm()
    return render(request , 'profile/index.html',  {"all_images": all_images ,"imageform":form  , "c_form": c_form , "comment": comment} )
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
            pic_id = int(request.POST.get('imageid'))
            pic = Image.objects.get(id=pic_id)
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = pic
            new_comment.save()
            
        return redirect('homepage')

    
# function  for returning image when clicked
def image_details(request , id):
    one_image = Image.objects.get(id = id)
    print(request)
    return render(request , 'profile/image.html' , {"one_image": one_image})

    # function of likes
def imagelike(request ):
    photo = get_object_or_404(Image , id=request.POST.get('id'))
    if photo.likes.filter(id = request.user.id).exists():
        photo.likes.remove(request.user)
        is_liked = False
    else:
        photo.likes.add(request.user)
        is_liked = True
        return HttpResponseRedirect(reverse('image_post'))

    