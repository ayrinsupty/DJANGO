from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def handlesignup(request):
        if request.method=="POST":
            uname = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("pass1")
            confirmpassword = request.POST.get("pass2")
            # print(uname, email, password, confirmpassword)
            if password != confirmpassword:
                messages.warning(request, "Password doesn't match!")
                return redirect('/signup')
            
            try:    
                if User.objects.get(username = uname):
                    messages.info(request, "Username is not available!")
                    return redirect('/signup')
            except:
                pass
            
            try:    
                if User.objects.get(email = email):
                    messages.info(request, "Email already exists!")
                    return redirect('/signup')
            except:
                pass
            
            myuser = User.objects.create_user(uname, email, password)
            myuser.save()
            
            messages.success(request, "Signed up successfully! Please log in!")
            return redirect('/login')
            
        return render(request,'signup.html')
    
def handlelogin(request):
        if request.method=="POST":
            uname=request.POST.get("username")
            pass1=request.POST.get("pass1")
            myuser=authenticate(username=uname,password=pass1)
            if myuser is not None:
                login(request,myuser)
    
                messages.success(request, "Logged in successfully!")
                return redirect('/')
            else:
                messages.error(request, "Invalid Credentials")
                return redirect('/login')
        
        return render(request,'login.html')
    
    
def handlelogout(request):
    logout(request)
    messages.info(request, "Sucessfully logged out!")
    return redirect('/login')