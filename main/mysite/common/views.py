from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Profile

def index(request):
    return render(request, 'main.html')

def register(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
                email=request.POST["email"]
            )
            profile = Profile(
                user=user,
                name=request.POST["name"],
                # is_admin=request.POST.get('is_admin', '') == 'on'
            )
            profile.save()
            return render(request, 'common/register_done.html', {'user': user})
        else:
            return HttpResponse("Passwords do not match")
    else:
        return render(request, 'common/register.html')



def change(request):
    if request.method == "POST":
        profile = Profile.objects.get(user=request.user)
        profile.name = request.POST["name"]
        # profile.is_admin = request.POST.get('is_admin', '') == 'on'
        profile.save()
        return redirect('/')
    else:
        return render(request, 'common/change.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        redirect('home')
    return render(request,'main.html')

# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .models import Profile
# from django.contrib.auth.models import User

# def index(request):
#     return render(request, 'main.html')

# def register(request):
#     if request.method == "POST":
#         if request.POST["password1"] == request.POST["password2"]:
#             user = User.objects.create_user(
#                 username=request.POST["username"],
#                 password=request.POST["password1"],
#                 email=request.POST["email"])
#             profile = Profile(
#                 user=user,
#                 name=request.POST["name"],
#                 is_admin=request.POST.get('is_admin', '') == 'on')
#             profile.save()
#             return redirect('/')
#     else:
#         return render(request, 'common/register.html')


# def change(request):
#     if request.method == "POST":
#         profile = Profile.objects.get(user=request.user)
#         profile.name = request.POST["name"]
#         profile.is_admin = request.POST.get('is_admin', '') == 'on'
#         profile.save()
#         return redirect('/')
#     else:
#         return render(request, 'common/change.html')

# #Create your views here.
