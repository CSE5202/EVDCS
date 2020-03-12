from django.urls import path

from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('auth', views.login_view, name='signin'),
    path('show',views.show,name='registerList'),  
    path('edit/<int:id>', views.edit,name='userEdit'),  
    path('update/<int:id>', views.update,name='userUpdate'),  
    path('delete/<int:id>', views.destroy,name='userDelete'),  
]