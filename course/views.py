from django.views import View
from .models import *
from django.contrib import messages
from django.shortcuts import render


def newcourse(request):
    if request.method == 'POST':
        product = request.POST.get('paid')
        cart = request.session.get('cart')
        if cart:
            cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            request.session['cart'] = cart
    cour = PaidCourse.objects.all()[0:4]
    pri = PricePlan.objects.all()[0:3]
    context = {'cour':cour,'price': pri}
    return render(request,'temp/index.html',context)

def productView(request, myid):
    product = PaidCourse.objects.filter(id=myid)
    context = {'products' :product[0]}
    return render(request, 'temp/view.html', context)


def allcourse(request):
    if request.method == 'POST':
        product = request.POST.get('paid')
        cart = request.session.get('cart')
        if cart:
            cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
            request.session['cart'] = cart
    cour = PaidCourse.objects.order_by('-id')
    context = {'cour':cour}
    return render(request,'temp/class.html',context)