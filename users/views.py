from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile

def login_profile(request):
    if request.method == "POST":
        
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(username = email, password = password )
        
        if user is not None:
            
            login(request, user)
            
            return redirect("index")
        else:
            print("Nimadir xato")
    else:
        return render(request, "login.html")
    
def profile(request):
    return render(request, "profile.html")

def user_logout(request):
    logout(request)
    
    return redirect("login_profile")


def user_sign(request):
    if request.method == "POST":
        
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        
       
        user = UserProfile.objects.filter(email=email)
       
        
        if user is not None:
            return render(request, "signup.html")
        
        new_user = UserProfile.objects.create_user(
            first_name= first_name,
            last_name= last_name,
            email = email,
            password=password
        )

        return render(request, "login.html")
        
        
        
        
    else:
        return render(request, "signup.html")