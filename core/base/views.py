from django.shortcuts import render ,redirect
from django.contrib.auth import login ,authenticate ,logout
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages
# Create your views here.

def index(request):
    context = {

        
    }
    return render(request, 'base/index.html')

def register_request(request):
    context={
        
    }
    return render(request,'base/register.html',context)

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f" {username} اهلا تم تسجيل دخولك بنجاح ")
                return redirect(index)
            else:
                messages.error(request,"كلمة مرور او اسم المستخدم خاطئ")
        else:
            messages.error(request,"كلمة مرور او اسم المستخدم خاطئ")
        form = AuthenticationForm()
    context={
        
    }
    return render(request,'base/login.html',context)

def logout_request(request):
    context={
        
    }
    return render(request,'base/logout.html',context)
