
from django.shortcuts import render

from django.contrib import messages

# Create your views here.

def start(request):
    return render(request,"blog/index.html")

def allposts(request):
    return render(request,"blog/posts.html")

def post(request):
    return "ho"

def contact(request):
    if request.method == 'POST':
        messages.success(request, "Message sent.")
    
    return render(request,"blog/contact.html")

def about(request):
    return render(request,"blog/about.html")