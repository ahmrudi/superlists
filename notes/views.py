from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login/')
def home_page(request):
    return render(request, 'notes/home.html')

def login_user(request):
    page_title = "Login"
    site_name = "Notes"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/notes/')
        else:
            return redirect('/error/')
    return render(request, 'notes/login.html', locals())

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/')

def sign_up(request):
    return render(request, 'notes/signup.html')

def error(request):
    return HttpResponse("error")