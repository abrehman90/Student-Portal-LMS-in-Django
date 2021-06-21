from django.contrib import admin
from authy.models import Profile
# Register your models here.


class admin_profile(admin.ModelAdmin):
    list_display = ['user','select']

    class Meta:
        model = Profile


admin.site.register(Profile,admin_profile)