from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

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

def handlelogin(request):
    return render(request,'login.html')

def handlesignup(request):
        if request.method=="POST":
            uname = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("pass1")
            confirmpassword = request.POST.get("pass2")
            # print(uname, email, password, confirmpassword)
            if password != confirmpassword:
                return HttpResponse("Password doesn't match!")
            
            try:    
                if User.objects.get(username = uname):
                    return HttpResponse("Username is not available!")
            except:
                pass
            try:    
                if User.objects.get(email = email):
                    return HttpResponse("Email already exists!")
            except:
                pass
            
            myuser = User.objects.create_user(uname, email, password)
            myuser.save()
            return HttpResponse("Signed up successfully!")
        return render(request,'signup.html')