#from django.db import models
from django.contrib.gis.db import models 

# Create your models here.
from django.contrib.auth.models import User
import datetime


class profile(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	sex = models.CharField(max_length=200,choices=(('male','male'),('female','female')))
	phone = models.CharField(max_length=200)
	age = models.PositiveIntegerField()
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return self.first_name + '  '+ self.last_name
class driver(models.Model):
	profile_id = models.ForeignKey('profile', on_delete=models.CASCADE)
	driver_licence = models.CharField(max_length=200,unique=True)
	licence_issued_date = models.DateTimeField('issued date')
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return self.profile_id.first_name +"  "+self.driver_licence
class subcity(models.Model):
    subcity_name = models.CharField(max_length=200)
    Number_Of_Station = models.PositiveIntegerField()
    Number_Of_Machine = models.PositiveIntegerField()
    Number_Of_Root =  models.PositiveIntegerField()
    Number_Of_Vehicles =  models.PositiveIntegerField()
    reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
    def __str__(self):
    	return self.subcity_name
class vehicle(models.Model):
	vehicle_name = models.CharField(max_length=200)
	driver = models.ForeignKey('driver', on_delete=models.CASCADE)
	plate_no = models.CharField(max_length=200,unique=True)
	model = models.CharField(max_length=200)
	vehicle_size = models.PositiveSmallIntegerField()
	subcity = models.ForeignKey('subcity', on_delete=models.CASCADE, default=None)
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return self.plate_no
class penalty(models.Model):
	penalty_type = models.CharField(max_length=200)
	#driver_licence  = models.ForeignKey('driver', on_delete=models.CASCADE)
	vehicle_plate = models.CharField(max_length=200)
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	trip_no =  models.IntegerField(null=True)
	phone = models.CharField(max_length=200,null=True)
	def __str__(self):
		return self.penalty_type
"""class location(models.Model):
	lattitude = models.FloatField()
	longitude = models.FloatField()
	
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.lattitude+ ' by '+ self.longitude"""


class station(models.Model):
	station_name = models.CharField(max_length=200)
	Number_Of_Root =  models.PositiveIntegerField()
	location = models.PointField()
	subcity =models.ForeignKey('subcity', on_delete=models.CASCADE)
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return self.station_name
class machine(models.Model):
	machine_id = models.CharField(max_length=200,unique=True)
	station_id = models.ForeignKey('station', on_delete=models.CASCADE)
	location = models.PointField()
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return self.machine_id
class machine_data(models.Model):
	destination= models.CharField(max_length=200)
	machineID = models.CharField(max_length=200)
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return self.destination
class route(models.Model):
	route_type = models.CharField(max_length=200,default="normal")
	length = models.CharField(max_length=200)
	price = models.FloatField()
	source = models.ForeignKey('station', on_delete=models.CASCADE, related_name="source")
	destination = models.ForeignKey('station', on_delete=models.CASCADE, related_name="dest")
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return self.source.station_name+" to "+ self.destination.station_name
class RouteTypes(models.Model):
    name = models.CharField(primary_key=True, max_length=20)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True)
    def __str__(self):
    	return self.name

    class Meta:
        db_table = 'route_types'
class deployment(models.Model):
	route_id = models.ForeignKey('route', on_delete=models.CASCADE)
	rounde = models.PositiveIntegerField()
	vehicle_plate = models.ForeignKey('vehicle', on_delete=models.CASCADE)
	route_type = models.CharField(max_length=20, null = True)
	route_length = models.CharField(max_length=200, null = True)
	route_price = models.FloatField(null = True)
	source_name = models.CharField(max_length=200, null = True)
	deestination_name = models.CharField(max_length=200, null = True)
	phone = models.CharField(max_length=200,null=True)

	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return self.vehicle_plate.plate_no+ ' by '+ str(self.route_id)
class waiting_time(models.Model):
	route_id = models.ForeignKey('route', on_delete=models.CASCADE)
	coming_time = models.DateTimeField('coming_time')
	going_time = models.DateTimeField('going_time')
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	def __str__(self):
		return str(self.route_id)
"""class vehicle_request(models.Model):
	station_id = models.ForeignKey('station', on_delete=models.CASCADE)
	route_id = models.ForeignKey('route', on_delete=models.CASCADE)
	machine_id = models.ForeignKey('machine', on_delete=models.CASCADE)
	subcity_name = models.ForeignKey('subcity', on_delete=models.CASCADE)
	request_date = models.DateTimeField('date requested')
	def __str__(self):
		return self.station_id+ ' by '+ self.route_id"""
class vehicles_location(models.Model):
	location = models.PointField()
	vehicle_id = models.ForeignKey('vehicle', on_delete=models.CASCADE)
	reg_date = models.DateTimeField('date registerd',default=datetime.datetime.now())
	device_id = models.CharField(max_length=200)
	def __str__(self):
		return self.device_id
class assign_vehicle(models.Model):
	length = models.CharField(max_length=200)
	source = models.CharField(max_length=200)
	destination = models.CharField(max_length=200)
	price = models.CharField(max_length=200)
	vehicles_id = models.ForeignKey('vehicle', on_delete=models.CASCADE)
	assign_date = models.DateTimeField('date assigned',default=datetime.datetime.now())
	status = models.CharField(max_length=200,default="pending")
	def __str__(self):
		return self.status


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    #driver = models.ForeignKey(Driver,on_delete=models.CASCADE)
    driver = models.CharField(max_length=20)
    trip_no = models.IntegerField()
    phone = models.CharField(max_length=200,null=True)
    
    
    class Meta0:
        db_table = 'attendance'
