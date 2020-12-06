from django.shortcuts import render,redirect
from django.http import HttpResponse
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
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import action
from django.views import generic
from django.contrib.gis.geos import fromstr,Point
from django.contrib.gis  .db.models.functions import Distance

from django.contrib.gis.geos import GEOSGeometry
from rest_framework.response import Response
from pyfcm import FCMNotification
from fcm_django.models import FCMDevice
from .forms import *
from .models import *
import folium
from folium import features



User = get_user_model()


# Create your views here.

def index(request):
   return render(request, "cityadmin/template/login.html", {})
@login_required
def register(request):
  
   return render(request, "registration/register.html", {})
@login_required
def driver_register(request):
  profile_obj = profile.objects.all()
  context = {'profile': profile_obj}
  return render(request, 'cityadmin/template/driver/register_driver.html', context)
@login_required
def driver_list(request):
  profile_obj = profile.objects.all()
  drivers=driver.objects.all()
  context = {'profile': profile_obj,'driver':drivers}
  return render(request, 'cityadmin/template/driver/driver_list.html', context)  
@login_required
def driver_register_save(request):
  
  if request.method == 'POST':
    profile_id=request.POST['profile_id']
    profile_obj = profile.objects.get(id=profile_id)
    driver_license=request.POST['driver_license']
    issued_date=request.POST['licence_issued_date']
    date_registerd=request.POST['reg_date'] 
    drive=driver(profile_id=profile_obj,driver_licence=driver_license,licence_issued_date=issued_date,reg_date=date_registerd)
    drive.save()
    return render(request, 'cityadmin/template/driver/register_driver.html')
  else:
   return render(request, 'cityadmin/template/driver/register_driver.html', context)
@login_required
def subcity_register(request):
  profile_obj = profile.objects.all()
  context = {'profile': profile_obj}
  return render(request, 'cityadmin/template/subcity/add_subcity.html', context)
@login_required
def subcity_list(request):
  Subcity_obj = subcity.objects.all()
  context = {'subcity': Subcity_obj}
  return render(request, 'cityadmin/template/subcity/subcity_list.html', context) 
@login_required 
def subcity_save(request):
  
  if request.method == 'POST':
    name=request.POST['name']
    No_station=request.POST['Number_Of_Station']
    no_machine=request.POST['Number_Of_Machine']
    no_root=request.POST['Number_Of_Root'] 
    no_vehicles=request.POST['Number_Of_Vehicles'] 
    sub=subcity(subcity_name=name,Number_Of_Station=No_station,Number_Of_Machine=no_machine,Number_Of_Root=no_root,Number_Of_Vehicles=no_vehicles)
    sub.save()
    messages.success(request,'successfully subcity is added')
    return redirect('subcity_register')
  else:
   return render(request, 'cityadmin/template/subcity/add_subcity.html', context)
@login_required
def subcity_edit(request,id):
    subcity_list = subcity.objects.get(id=id)
    context = {'subcity': subcity_list}
    return render(request, 'cityadmin/template/subcity/update_subcity.html', context)
@login_required
def subcity_update(request,id):
    subcity_list = subcity.objects.get(id=id)
    
    context = {'subcity': subcity_list}
    f = subcityForm(request.POST,instance=subcity_list)
    if f.is_valid():
      f.save()
      messages.success(request, 'subcity updated successfully')
      return redirect('subcity_list')  
    return render(request, 'cityadmin/template/subcity/update_subcity.html', context)
@login_required
def subcity_destroy(request,id):
    subcity_list = subcity.objects.get(id=id)
    subcity_list.delete()
    context = {'subcity': subcity}
    return redirect('subcity_list')  

@login_required
def station_register(request):
  sub_obj = subcity.objects.all()
  context = {'subcity': sub_obj}
  return render(request, 'cityadmin/template/station/add_station.html', context)
@login_required
def station_list(request):
  Subcity_obj = station.objects.all()
  context = {'station': Subcity_obj}
  return render(request, 'cityadmin/template/station/station_list.html', context)
@login_required
def station_save(request):
  if request.method == 'POST':
    name=request.POST['name']
    lat=float(request.POST['lat'])
    longi=float(request.POST['long'])
    no_root=request.POST['Number_Of_Root'] 
    subcity_id=request.POST['subcity_id'] 
    location=Point(longi,lat,srid=4326)
    sub=station(station_name=name,Number_Of_Root=no_root,subcity_id=subcity_id,location=location)
    sub.save()
    messages.success(request,'successfully station is added')
    return redirect('station_register')
  else:
   return render(request, 'cityadmin/template/station/add_station.html', context)
@login_required
def station_edit(request,id):
    station_list = station.objects.get(id=id)
    Subcity_obj = station.objects.all()
    context = {'station': station_list,'subcity':Subcity_obj}
    return render(request, 'cityadmin/template/station/update_station.html', context)
@login_required
def station_update(request,id):
  station_list = station.objects.get(id=id)
  if request.method == 'POST':
    name=request.POST['name']
    lat=float(request.POST['lat'])
    longi=float(request.POST['long'])
    no_root=request.POST['Number_Of_Root'] 
    subcity_id=request.POST['subcity_id'] 
    sub1=subcity.objects.get(id=subcity_id)
    location=Point(longi,lat,srid=4326)
    station_list.station_name=name
    station_list.Number_Of_Root=no_root
    station_list.subcity=sub1
    #sub=station_list.update(station_name=name,Number_Of_Root=no_root,subcity_id=subcity_id,location=location)
    station_list.save()
    messages.success(request,'successfully station is updated')
    return redirect('station_list')
  else:
   return render(request, 'cityadmin/template/station/add_station.html', context)

@login_required   
def station_destroy(request,id):
    station_list = station.objects.get(id=id)
    station_list.delete()
    context = {'station': station}
    return redirect('station_list')  




@login_required
def route_register(request):
  station_obj = station.objects.all()
  context = {'station': station_obj}
  return render(request, 'cityadmin/template/route/add_route.html', context)
@login_required
def route_list(request):
  Subcity_obj = route.objects.all()
  context = {'route': Subcity_obj}
  return render(request, 'cityadmin/template/route/route_list.html', context)
@login_required 
def route_save(request):
  if request.method == 'POST':
      f = routeForm(request.POST)
      if f.is_valid():
          f.save()
          messages.success(request,'successfully route is added')
          return redirect('route_register')

  else:
   return render(request, 'cityadmin/template/route/add_route.html', context)

@login_required
def route_edit(request,id):
    station_obj = station.objects.all()
    route_list = route.objects.get(id=id)
    context = {'route': route_list,'station': station_obj}
    return render(request, 'cityadmin/template/route/update_route.html', context)
@login_required
def route_update(request,id):
    route_list = route.objects.get(id=id)
    
    context = {'route': route_list}
    f = routeForm(request.POST,instance=route_list)
    if f.is_valid():
      f.save()
      messages.success(request, 'route updated successfully')
      return redirect('route_list')  
    return render(request, 'cityadmin/template/route/update_route.html', context)
@login_required
def route_destroy(request,id):
    route_list = route.objects.get(id=id)
    route_list.delete()
    context = {'route': route}
    return redirect('route_list')  

@login_required
def Assigned_vehicle_list(request):
  vehicle_obj = vehicle.objects.all()
  context = {'vehicle': vehicle_obj}
  return render(request, 'cityadmin/template/vehicle/assigned_vehicle_list.html', context)  
@login_required
def vehicle_register(request):
  sub_obj = subcity.objects.all()
  driver_obj=driver.objects.all()
  context = {'subcity': sub_obj,'driver':driver_obj}
  return render(request, 'cityadmin/template/vehicle/add_vehicle.html', context)
@login_required
def vehicle_list(request):
  vehicle_obj = vehicle.objects.all()
  context = {'vehicle': vehicle_obj}
  return render(request, 'cityadmin/template/vehicle/vehicle_list.html', context)
@login_required
def vehicle_save(request):
  if request.method == 'POST':
      f = vehicleForm(request.POST)
      if f.is_valid():
          f.save()
          messages.success(request,'successfully vehicle is added')
          return redirect('vehicle_list')

  else:
   return render(request, 'cityadmin/template/vehicle/add_vehicle.html', context)
   
@login_required
def vehicle_edit(request,id):
    sub_obj = subcity.objects.all()
    driver_obj=driver.objects.all()
    vehicle_list = vehicle.objects.get(id=id)
    context = {'vehicle': vehicle_list,'station': sub_obj,'subcity': sub_obj,'driver':driver_obj}
    return render(request, 'cityadmin/template/vehicle/update_vehicle.html', context)

@login_required
def vehicle_update(request,id):
    vehicle_list = vehicle.objects.get(id=id)
    
    context = {'vehicle': vehicle_list}
    f = vehicleForm(request.POST,instance=vehicle_list)
    if f.is_valid():
      f.save()
      messages.success(request, 'vehicle updated successfully')
      return redirect('vehicle_list')  
    return render(request, 'cityadmin/template/vehicle/update_vehicle.html', context)

@login_required
def vehicle_destroy(request,id):
    vehicle_list = vehicle.objects.get(id=id)
    vehicle_list.delete()
    context = {'vehicle': vehicle}
    return redirect('vehicle_list')


@login_required
def vehicle_location(request):
    Latlon=vehicles_location.objects.all()
    
    m = folium.Map(location=[9.017167,38.795471], height=800,width=1200,zoom_start=13)
    for i in Latlon:
      lat=i.location.centroid.y
      lon=i.location.centroid.x
      v_id=i.vehicle_id
    
      mk=features.Marker([lat, lon])

      pp = folium.Popup(v_id)
      ic = features.Icon(color='blue',icon="fa-bus", prefix='fa')

      mk.add_child(ic)
      mk.add_child(pp)
      m.add_child(mk)
    m=m._repr_html_()
    context = {'map': m}
    return render(request, 'cityadmin/template/vehicle/vehicle_location.html', context)
@login_required
def location(request,mid):
    i=machine.objects.get(machine_id=mid)
    lat=i.location.centroid.y
    lon=i.location.centroid.x
    
    m = folium.Map(location=[lat,lon], height=800,width=1200,zoom_start=13)

      
    v_id=i.machine_id
    print(lat,lon)
    mk=features.Marker([lat, lon])

    pp = folium.Popup(v_id)
    ic = features.Icon(color='blue',icon="fa-bus", prefix='fa')

    mk.add_child(ic)
    mk.add_child(pp)
    m.add_child(mk)
    m=m._repr_html_()
    context = {'map': m}
    return render(request, 'cityadmin/template/vehicle/vehicle_location.html', context)
@login_required
@login_required
def machine_register(request):
  station_obj = station.objects.all()
 
  context = {'station': station_obj}
  return render(request, 'cityadmin/template/machine/add_machine.html', context)
@login_required
def machine_list(request):
  machine_obj = machine.objects.all()
  context = {'machine': machine_obj}
  return render(request, 'cityadmin/template/machine/machine_list.html', context) 

@login_required 
def machine_data_list(request):
  machine_obj = machine_data.objects.all()
  context = {'machine': machine_obj}
  return render(request, 'cityadmin/template/machine/machine_data_list.html', context)

@login_required
def machine_save(request):
  if request.method == 'POST':
    ma_id=request.POST['machine_id']
    lat=float(request.POST['lat'])
    longi=float(request.POST['long'])
    station_id=request.POST['station_id'] 
    station_ob=station.objects.get(id=station_id)
    location=Point(longi,lat,srid=4326)
    machi=machine(machine_id=ma_id,station_id=station_ob,location=location)
    machi.save()
    messages.success(request,'successfully machine is added')
    return redirect('machine_list')

  else:
   return render(request, 'cityadmin/template/machine/add_machine.html', context)
@login_required
def machine_edit(request,id):
    sub_obj = subcity.objects.all()
    driver_obj=driver.objects.all()
    machine_list = machine.objects.get(id=id)
    context = {'machine': machine_list,'station': sub_obj,'subcity': sub_obj,'driver':driver_obj}
    return render(request, 'cityadmin/template/machine/update_machine.html', context)
@login_required   
def machine_update(request,id):
    machine_list = machine.objects.get(id=id)
    
    context = {'machine': machine_list}
    f = machineForm(request.POST,instance=machine_list)
    if f.is_valid():
      f.save()
      messages.success(request, 'machine updated successfully')
      return redirect('machine_list')  
    return render(request, 'cityadmin/template/machine/update_machine.html', context)
@login_required
def machine_destroy(request,id):
    machine_list = machine.objects.get(id=id)
    machine_list.delete()
    context = {'machine': machine}
    return redirect('machine_list')