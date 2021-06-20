from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from  django.contrib import messages
# Create your views here.


def indexshow(request):
    # context = {}
    return render(request,'temp/index.html')


# @login_required(login_url="login")
# def classes(request):
#     context = {}
#     return render(request,'class.html',context)
#
#
# @login_required(login_url="login")
# def assigment(request):
#     context = {}
#     return render(request,'class.html',context)


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

#
# def price(request):
#     context = {}
#     return render(request,'price.html',context)
#
#
# @login_required(login_url="login")
# def services(request):
#     context = {}
#     return render(request,'about.html',context)
#
#
# def detail(request):
#     context = {}
#     return render(request,'about.html',context)


def team(request):
    context = {}
    return render(request,'temp/team.html',context)


def about(request):
    context = {}
    return render(request,'temp/about.html',context)