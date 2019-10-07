from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['password_confirmation']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken!!')
                return redirect('/accounts/register'); 
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken!!')
                return redirect('accounts/register'); 
            else:
                user = User.objects.create_user(first_name=first_name, password=password1, email=email, last_name=last_name, username=username)
                user.save();
                messages.info(request, 'User Created!!')
        else:
            messages.info(request, 'Password Not Matching!!')
            return redirect('accounts/register'); 
        
        return redirect('/courses'); 
    else:   
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/courses')
        else:
            messages.info(request, 'Login failed!!')
            return redirect('login'); 
        
        return redirect('/courses'); 
    else:   
        return render(request, 'accounts/login.html')

def logout(request):
    
    auth.logout(request)
    return redirect('/courses'); 
