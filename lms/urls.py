

from django.urls import path
from .views import *

urlpatterns = [
    path('',indexshow,name='indexshow'),
    path('contact/',contact,name='contact'),
    path('team/',team,name='team'),
    path('about/',about,name='about'),
]
