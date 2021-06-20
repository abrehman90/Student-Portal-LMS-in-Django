from django.contrib import admin
from .models import *
# Register your models here.


class Contactadmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject']
    list_per_page = 15


admin.site.register(Contact,Contactadmin)