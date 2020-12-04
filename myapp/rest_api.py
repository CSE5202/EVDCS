from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, Group
import time
from rest_framework import viewsets,status
from rest_framework import permissions
from .serializers import *

from django.contrib import messages 
# Create your views here.
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from accounts.models import Phonenumber

from rest_framework.decorators import action
from django.views import generic
from django.contrib.gis.geos import fromstr,Point
from django.contrib.gis  .db.models.functions import Distance

from django.contrib.gis.geos import GEOSGeometry
from rest_framework.response import Response
from pyfcm import FCMNotification
from fcm_django.models import FCMDevice
from .forms import *
User = get_user_model()

def send_notification(device_id,data):
   try:
      device = FCMDevice.objects.all()
      print(device)
      result = device.send_message(title="This is Ride Request",body="Accept Ride Request",
                          data=data,sound=True)
     
      return result
   except:

      pass

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class driverViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = driver.objects.all()
    serializer_class = driverSerializer
    
class profileViewSet(viewsets.ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = profileSerializer
    
   

class PhonenumberViewSet(viewsets.ModelViewSet):
    queryset = Phonenumber.objects.all()
    serializer_class = PhonenumberSerializer

class assignmentViewSet(viewsets.ModelViewSet):
    queryset = assign_vehicle.objects.all()
    serializer_class = assignementSerializer
    

class deploymentViewSet(viewsets.ModelViewSet):
    queryset = deployment.objects.all()
    serializer_class = deploymentSerializer


class attendanceDataViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = attendanceSerializer
    

class penaltyDataViewSet(viewsets.ModelViewSet):
    queryset = penalty.objects.all()
    serializer_class = penaltySerializer

class stationDataViewSet(viewsets.ModelViewSet):
    queryset = station.objects.all()
    serializer_class = stationSerializer


class MachineDataViewSet(viewsets.ModelViewSet):
  
    serializer_class = MachineDataSerializer
    
    def get_queryset(self):
      queryset = machine_data.objects.all()
      return queryset
    def create(self, request, *args, **kwargs):
      machine_id=request.data['machineID']
      
      dest=request.data['destination']
      source= machine.objects.get(machine_id=machine_id).station_id.id

      destination= station.objects.get(station_name=dest).id

      print(source, destination)
      routes=route.objects.filter(source=source,destination=destination).first()
      

      s=routes.source.station_name
      de=routes.destination.station_name
      price=routes.price
      length=routes.length



      print(s,de,price,length)
     

      dest1=routes.destination.station_name
      print(dest1)

      


      machine_location = machine.objects.filter(machine_id=machine_id).first().location
      
      pnt = GEOSGeometry(machine_location)

      

      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
        

      self.perform_create(serializer)
 
      nearLocations = vehicles_location.objects.annotate(distance=Distance('location', pnt)).order_by('distance')[0:2]
      i=0
      for locat in nearLocations:
       
        vehicleidd=nearLocations[i].vehicle_id
        devices_id=nearLocations[i].device_id
        print(vehicleidd,devices_id,i)

           
        assign=assign_vehicle(source=s,destination=de,price=price,length=length, vehicles_id=vehicleidd)
        assign.save()
        data = {
         "source":s,
         "destination": de,
         "length": length,
         "price": price,
         "id":assign.id
                      }
        
        send_notification(device_id=devices_id,data=data)
        time.sleep(5)
        print(assign.id)
        
        if((assign_vehicle.objects.get(id=assign.id).status)=="accepted"):
          break


        i+=1
        
        

      
      
      headers = self.get_success_headers(serializer.data)
      return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
    
      serializer.save()
      


