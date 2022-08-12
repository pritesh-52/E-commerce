from unicodedata import category
from django.shortcuts import redirect, render
from django.http import  HttpResponse
from django.contrib import messages
from django.urls import is_valid_path
from django.contrib.auth import authenticate,login,logout

from store.forms import CustomUserForm


def register(request):   #register view
    form=CustomUserForm() #djano inbulit form use for register
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():   #check form as validd  or not
            form.save()   #save all data 
            messages.success(request,"Registred sucessfully ! Login continue")
            return redirect('/login')
    context={'form':form}
    return render(request,'store/auth/register.html',context)


def loginpage(request):   #login page 
    if request.user.is_authenticated:  #check user is loggein or not
        messages.warning(request,"You have already logged in")
        return redirect('/')
    else:
        if request.method == 'POST':   #othwerwise login
            name=request.POST.get('username')
            passw=request.POST.get('password')
            user=authenticate(request,username=name,password=passw)

            if user is not None:
                login(request,user)   #defayt login function provide
                messages.success(request,'Logined successfully')
                return redirect("/")
            else:
                messages.error(request,'Invalid username or password')
                return redirect('/login')
    return render(request,'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)  #budefault logout function provide
        messages.warning(request,"Logout successfully")
    return redirect("/")
