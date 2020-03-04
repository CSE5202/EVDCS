from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import profile,driver,route,machine,deployment,station,penalty,vehicle,waiting_time,assign_vehicle,subcity,vehicle_request,location

admin.site.register(profile)
admin.site.register(driver)
admin.site.register(route)
admin.site.register(machine)
admin.site.register(deployment)
admin.site.register(station)
admin.site.register(penalty)
admin.site.register(vehicle)
admin.site.register(waiting_time)
admin.site.register(assign_vehicle)
admin.site.register(subcity)
admin.site.register(vehicle_request)
admin.site.register(location)