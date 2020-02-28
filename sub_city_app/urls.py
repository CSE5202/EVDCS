from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='subcity-home'),
    path('register_driver/',views.register_driver,name='subcity-register_driver'),
]