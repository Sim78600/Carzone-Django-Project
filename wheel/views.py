from django.shortcuts import render
from django.http import request

# Create your views here.

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def serv(request):
    return render(request,'services.html')

def cont(request):
    return render(request,'contact.html')