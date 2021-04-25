from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='loginUser')
def home(request):
    if request.method=='POST':
        title = request.POST.get('title')
        status = request.POST.get('status')
        todo = Todo(title=title,status=status,user=request.user)
        if title:
            todo.save()

    data = Todo.objects.filter(user=request.user)
    context = {
        # 'todo':todo,
        'data':data,
    }
    return render(request,'TODO/home.html',context)

@login_required(login_url='loginUser')
def delete(request,pk):
    todo = Todo.objects.filter(id=pk)
    todo.delete()
    return redirect('/')


def register(request):
    errors=""
    flagF=0
    flagT=0
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if (not User.objects.filter(username=username).exists()) and (not User.objects.filter(email=email).exists()) and password and username and email: 
                user = User.objects.create_user(username,email,password)
                user.save()
                errors = "Registration Success"
                flagT=1
                return redirect('loginUser')
            else:
                errors = "Choose different username or email"
                flagF=1
    
    context = {
        'errors': errors,
        'flagF':flagF,
        'flagT':flagT,
    }
    return render(request,'TODO/register.html',context)


def loginUser(request):
    errors = ""
    flagF = 0
    flagT = 0
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                errors = "Login Success"
                flagT = 1
                return redirect('home')
            else:
                errors = "Invalid Username or Password"
                flagF = 1

    context = {
        'errors': errors,
        'flagF': flagF,
        'flagT': flagT,
    }
    return render(request, 'TODO/login.html',context)


@login_required(login_url='loginUser')
def logoutUser(request):
    logout(request)
    return redirect('loginUser')


####################################################################
####################################################################


# def register(request):
#     errors = ""
#     if request.method == 'POST':
#         user = TodoUser()
#         user.username = request.POST.get('username')
#         user.email = request.POST.get('email')
#         user.password = request.POST.get('password')
#         if (not TodoUser.objects.filter(username=user.username).exists()) and (not TodoUser.objects.filter(email=user.email).exists()):
#             user.save()
#         else:
#             errors = "Choose different username or email"
    
#     context = {
#         'errors': errors,
#     }
#     return render(request,'TODO/register.html',context)


# ####################################################################


# def loginUser(request):
#     errors = ""
#     if request.method == 'POST':
#         p=0
#         user = TodoUser.objects.all()
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         for i in user:
#             if i.username==username and i.password==password:
#                 p=1    
#                 break
        
#         if p:
#             user  = authenticate(username=username,password=password)
#             login(request,user)
#             errors = "Successful Login"
#             print(user)
#         else:
#             errors = "Invalid username or password"
#         # if password==passwordCheck:
#         #     login(request,username)
#         # else:
#         #     errors = "Invalid username or password"
#     context = {
#         'errors': errors,
#     }
#     return render(request,'TODO/login.html',context)


