from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import CustomLoginForm

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print(username)
            form.save()

            return redirect("/login")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})



def user_login(request):
    if request.method == "POST":
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page or wherever you want
                return redirect("/")
            else:
                # Authentication failed, display an error message
                form.add_error(None, "Invalid credentials")
    else:
        form = CustomLoginForm()

    return render(request, "registration/login.html", {"form": form})



def user_logout(request):
    logout(request)
    
    # Redirect to login page
    return redirect("login")

@login_required
def profile(request):
    return render(request, "registration/profile.html")
