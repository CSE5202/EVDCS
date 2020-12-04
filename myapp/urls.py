from django.urls import path

from . import views,deploy,chart,attendance,penality

urlpatterns = [
    path('showpenality/', penality.showpenality, name="showpenality"),
    path('takepenality/',  penality.takepenality, name="takepenality"),

    path('showattendance/', attendance.showattendance, name="showattendance"),
    path('takeattendance/', attendance.takeattendance, name="takeattendance"),


    path('report', chart.report, name='report'),
    path('report-chart/', chart.report_chart, name='report-chart'),
    path('', views.index, name='index'),
 
    path('vehicle_location', views.vehicle_location,name='vehicle_location'),
    path('location/<str:mid>', views.location,name='location'),



    path('deployment', deploy.deploy,name="deploy"),
    path('driver/register', views.driver_register, name='driver_register'),
    path('driver/new', views.driver_register_save, name='driver_save'),
    path('driver/', views.driver_list, name='driver_list'),


    path('subcity/register', views.subcity_register, name='subcity_register'),
    path('subcity/new', views.subcity_save, name='subcity_save'),
    path('subcity/', views.subcity_list, name='subcity_list'),
    path('subcity/edit/<int:id>', views.subcity_edit,name='subcityEdit'),  
    path('subcity/update/<int:id>', views.subcity_update,name='subcityUpdate'),  
    path('subcity/delete/<int:id>', views.subcity_destroy,name='subcityDelete'),  

    path('station/register', views.station_register, name='station_register'),
    path('station/new', views.station_save, name='station_save'),
    path('station/', views.station_list, name='station_list'),
    path('station/edit/<int:id>', views.station_edit,name='stationEdit'),  
    path('station/update/<int:id>', views.station_update,name='stationUpdate'),  
    path('station/delete/<int:id>', views.station_destroy,name='stationDelete'), 


    path('route/register', views.route_register, name='route_register'),
    path('route/new', views.route_save, name='route_save'),
    path('route/', views.route_list, name='route_list'),
    path('route/edit/<int:id>', views.route_edit,name='routeEdit'),  
    path('route/update/<int:id>', views.route_update,name='routeUpdate'),  
    path('route/delete/<int:id>', views.route_destroy,name='routeDelete'), 


    path('vehicle/register', views.vehicle_register, name='vehicle_register'),
    path('vehicle/new', views.vehicle_save, name='vehicle_save'),
    path('vehicle/', views.vehicle_list, name='vehicle_list'),
    path('Assigned_vehicle_list/', views.Assigned_vehicle_list, name='Assigned_vehicle_list'),
    path('vehicle/edit/<int:id>', views.vehicle_edit,name='vehicleEdit'),  
    path('vehicle/update/<int:id>', views.vehicle_update,name='vehicleUpdate'),  
    path('vehicle/delete/<int:id>', views.vehicle_destroy,name='vehicleDelete'),  

    path('machine/register', views.machine_register, name='machine_register'),
    path('machine/new', views.machine_save, name='machine_save'),
    path('machine/', views.machine_list, name='machine_list'),
    path('machine/edit/<int:id>', views.machine_edit,name='machineEdit'),  
    path('machine/update/<int:id>', views.machine_update,name='machineUpdate'),  
    path('machine/delete/<int:id>', views.machine_destroy,name='machineDelete'),
    path('machine/data', views.machine_data_list, name='machine_data_list'), 


]