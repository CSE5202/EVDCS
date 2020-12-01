from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Phonenumber 

admin.site.register(Phonenumber)

admin.site.register(User)