from django.urls import path
from .views import *
from django.conf.urls import url


app_name = 'shopping_cart'

urlpatterns = [
    path('',newcourse,name='coursepaid'),
    path('allclasses/',allcourse,name='coursepaid'),
    path('courseview/<int:myid>',productView,name='productview'),
]
