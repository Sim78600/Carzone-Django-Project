from django.shortcuts import render , redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
from contact.models import Contact
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    if request.method == 'POST':
        un = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(username=un,password=pw)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
         fn = request.POST['firstname']
         ln = request.POST['lastname']
         un = request.POST['username']
         em = request.POST['email']
         pw = request.POST['password']
         cp = request.POST['confirm_password']
         if pw == cp:
            if User.objects.filter(username=un).exists():
                messages.error(request,'Username already exists !')
                return redirect('signup')
            else:
                if User.objects.filter(email=em).exists():
                    messages.error(request,'Email already in use !')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(first_name=fn,last_name=ln,username=un,email=em,password=pw)
                    auth.login(request,user)
                    messages.success(request," You are now logged in.")
                    return redirect("dashboard")
                    user.save()
                    messages.success(request,"You are registered successfully")
                    return redirect('login')
        
         else:
            messages.error(request,'Passwords do not match')
            return redirect('signup')
    else:
        return render(request,'signup.html')
        
@login_required(login_url='login')
def dashboard(request):
    user_inquiry = Contact.objects.order_by('create_date').filter(user_id=request.user.id)
    data = {
        'inquiries' : user_inquiry
    }
    return render(request,'dashboard.html',data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')
