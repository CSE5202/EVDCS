from django.urls import path

from . import views,deploy,chart,attendance,penality

urlpatterns = [
    path('showpenality/', penality.showpenality, name="Subcity_showpenality"),
    path('takepenality/',  penality.takepenality, name="Subcity_takepenality"),

    path('showattendance/', attendance.showattendance, name="Subcity_showattendance"),
    path('takeattendance/', attendance.takeattendance, name="Subcity_takeattendance"),


    path('report', chart.report, name='Subcity_report'),
    path('report-chart/', chart.report_chart, name='Subcity_report-chart'),
    path('', views.index, name='Subcity_index'),
 
    path('vehicle_location', views.vehicle_location,name='Subcity_vehicle_location'),
    path('location/<str:mid>', views.location,name='Subcity_location'),

    path('deployment', deploy.deploy,name="Subcity_deploy"),
    path('driver/register', views.driver_register, name='Subcity_driver_register'),
    path('driver/new', views.driver_register_save, name='Subcity_driver_save'),
    path('driver/', views.driver_list, name='Subcity_driver_list'),


    path('subcity/register', views.subcity_register, name='Subcity_subcity_register'),
    path('subcity/new', views.subcity_save, name='Subcity_subcity_save'),
    path('subcity/', views.subcity_list, name='Subcity_subcity_list'),
    path('subcity/edit/<int:id>', views.subcity_edit,name='Subcity_subcityEdit'),  
    path('subcity/update/<int:id>', views.subcity_update,name='Subcity_subcityUpdate'),  
    path('subcity/delete/<int:id>', views.subcity_destroy,name='Subcity_subcityDelete'),  

    path('station/register', views.station_register, name='Subcity_station_register'),
    path('station/new', views.station_save, name='Subcity_station_save'),
    path('station/', views.station_list, name='Subcity_station_list'),
    path('station/edit/<int:id>', views.station_edit,name='Subcity_stationEdit'),  
    path('station/update/<int:id>', views.station_update,name='Subcity_stationUpdate'),  
    path('station/delete/<int:id>', views.station_destroy,name='Subcity_stationDelete'), 


    path('route/register', views.route_register, name='Subcity_route_register'),
    path('route/new', views.route_save, name='Subcity_route_save'),
    path('route/', views.route_list, name='Subcity_route_list'),
    path('route/edit/<int:id>', views.route_edit,name='Subcity_routeEdit'),  
    path('route/update/<int:id>', views.route_update,name='Subcity_routeUpdate'),  
    path('route/delete/<int:id>', views.route_destroy,name='Subcity_routeDelete'), 


    path('vehicle/register', views.vehicle_register, name='Subcity_vehicle_register'),
    path('vehicle/new', views.vehicle_save, name='Subcity_vehicle_save'),
    path('vehicle/', views.vehicle_list, name='Subcity_vehicle_list'),
    path('Assigned_vehicle_list/', views.Assigned_vehicle_list, name='Subcity_Assigned_vehicle_list'),
    path('vehicle/edit/<int:id>', views.vehicle_edit,name='Subcity_vehicleEdit'),  
    path('vehicle/update/<int:id>', views.vehicle_update,name='Subcity_vehicleUpdate'),  
    path('vehicle/delete/<int:id>', views.vehicle_destroy,name='Subcity_vehicleDelete'),  

    path('machine/register', views.machine_register, name='Subcity_machine_register'),
    path('machine/new', views.machine_save, name='Subcity_machine_save'),
    path('machine/', views.machine_list, name='Subcity_machine_list'),
    path('machine/edit/<int:id>', views.machine_edit,name='Subcity_machineEdit'),  
    path('machine/update/<int:id>', views.machine_update,name='Subcity_machineUpdate'),  
    path('machine/delete/<int:id>', views.machine_destroy,name='Subcity_machineDelete'),
    path('machine/data', views.machine_data_list, name='Subcity_machine_data_list'), 


]