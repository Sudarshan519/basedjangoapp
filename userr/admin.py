# Register your models here.
# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
admin.site.register(CustomUser)
# class CustomUserAdmin(UserAdmin):
#     model = Employer
#     list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']

# admin.site.register(Employer, CustomUserAdmin)