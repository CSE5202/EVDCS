from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello', views.hello, name='hello'),
    path('login', views.login_view, name='login'),
    path('auth', views.login_view1, name='signin'),
]