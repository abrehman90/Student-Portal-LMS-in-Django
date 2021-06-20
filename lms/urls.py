

from django.urls import path
from .views import *

urlpatterns = [
    path('',indexshow,name='indexshow'),
    # path('classes/',classes,name='classes'),
    path('contact/',contact,name='contact'),
    # path('services/',services,name='services'),
    # path('assigment/',assigment,name='assigment'),
    # # path('login/',sign,name='sign'),
    # path('price/',price,name='price'),
    # path('detail/',detail,name='detail'),
    path('team/',team,name='team'),
    path('about/',about,name='about'),
]
