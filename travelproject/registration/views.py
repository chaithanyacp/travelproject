
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages, auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pswd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['cpassword']
        email = request.POST['email']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken try another")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already registered try another")
                return redirect('register')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email= email)
                user.save();
                print("user created")
        else:
            messages.info(request,"Password Not matching")
            return redirect('register')
        return redirect('login')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')