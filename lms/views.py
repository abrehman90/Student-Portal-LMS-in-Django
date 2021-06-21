from django.shortcuts import render
from .models import *


def indexshow(request):
    return render(request,'temp/index.html')


def contact(request):
    if request.method == 'POST' and 'cont' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        bodymsg = request.POST['message']
        form = Contact(name=name,email=email,subject=subject,msg=bodymsg)
        form.save()
    context = {}
    return render(request,'temp/contact.html',context)


def team(request):
    context = {}
    return render(request,'temp/team.html',context)


def about(request):
    context = {}
    return render(request,'temp/about.html',context)