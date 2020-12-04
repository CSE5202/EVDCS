"""evdc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from rest_framework import routers
from myapp import views,rest_api


router = routers.DefaultRouter()
router.register(r'users', rest_api.UserViewSet)
router.register(r'drivers', rest_api.driverViewSet)
router.register('PhoneNumber', rest_api.PhonenumberViewSet,basename="PhoneNumber")
router.register(r'profile', rest_api.profileViewSet)
router.register('assign-vehicle', rest_api.assignmentViewSet)
router.register(r'Machine-data', rest_api.MachineDataViewSet,basename="Machine-data")
router.register(r'deployment', rest_api.deploymentViewSet)
router.register(r'attendance', rest_api.attendanceDataViewSet)
router.register(r'penalty', rest_api.penaltyDataViewSet)
router.register(r'station', rest_api.stationDataViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
]
