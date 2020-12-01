from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin


@admin.register(machine)
class MachineAdmin(LeafletGeoAdmin):
    list_display = ('machine_id', 'station_id','location')
@admin.register(machine_data)
class MachineDataAdmin(LeafletGeoAdmin):
    list_display = ('machineID', 'destination')

admin.site.register(profile)
admin.site.register(Attendance)

admin.site.register(driver)

admin.site.register(route)
admin.site.register(RouteTypes)
@admin.register(vehicles_location)
class vehicle_location_Admin(LeafletGeoAdmin):
    list_display = ('vehicle_id', 'location')

admin.site.register(deployment)
@admin.register(station)
class StationAdmin(LeafletGeoAdmin):
    list_display = ('station_name', 'subcity','location')
admin.site.register(penalty)
admin.site.register(vehicle)
admin.site.register(waiting_time)
admin.site.register(assign_vehicle)
admin.site.register(subcity)
