from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class profile(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	sex = models.CharField(max_length=200,choices=(('male','male'),('female','female')))
	phone = models.CharField(max_length=200)
	age = models.PositiveIntegerField()
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.first_name + ' by '+ self.last_name
class driver(models.Model):
	profile_id = models.ForeignKey('profile', on_delete=models.CASCADE)
	driver_licence = models.CharField(max_length=200,unique=True)
	licence_issued_date = models.DateTimeField('issued date')
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.driver_licence+ ' by '+ self.profile.profile_id
class vehicle(models.Model):
	vehicle_name = models.CharField(max_length=200)
	plate_no = models.CharField(max_length=200,unique=True)
	model = models.CharField(max_length=200,unique=True)
	vehicle_size = models.PositiveSmallIntegerField()
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.plate_no
class penalty(models.Model):
	penalty_type = models.CharField(max_length=200)
	driver_licence  = models.ForeignKey('driver', on_delete=models.CASCADE)
	vehicle_plate = models.ForeignKey('vehicle', on_delete=models.CASCADE)
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.driver.driver_licence+ ' by '+ self.penalty_type
class location(models.Model):
	lattitude = models.CharField(max_length=200)
	longitude = models.CharField(max_length=200)
	altitude = models.CharField(max_length=200)
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.lattitude+ ' by '+ self.longitude
class subcity(models.Model):
	subcity_name = models.CharField(max_length=200)
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.subcity_name

class station(models.Model):
	station_name = models.CharField(max_length=200)
	location_id = models.ForeignKey('location', on_delete=models.CASCADE)
	subcity =models.ForeignKey('subcity', on_delete=models.CASCADE)
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.subcity+ ' by '+ self.station_name
class machine(models.Model):
	machine_id = models.CharField(max_length=200,unique=True)
	station_id = models.ForeignKey('station', on_delete=models.CASCADE)
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.machine_id
class route(models.Model):
	route_type = models.CharField(max_length=200)
	length = models.CharField(max_length=200)
	source = models.ForeignKey('station', on_delete=models.CASCADE)
	#destination = models.ForeignKey('station', on_delete=models.CASCADE)
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.source #+ ' by '+ self.destination

class deployment(models.Model):
	route_id = models.ForeignKey('route', on_delete=models.CASCADE)
	vehicle_plate = models.ForeignKey('vehicle', on_delete=models.CASCADE)
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.vehicle_plate+ ' by '+ self.route_id
class waiting_time(models.Model):
	machine_id = models.ForeignKey('machine', on_delete=models.CASCADE)
	coming_time = models.DateTimeField('coming_time')
	going_time = models.DateTimeField('going_time')
	reg_date = models.DateTimeField('date registerd')
	def __str__(self):
		return self.machine_id
class vehicle_request(models.Model):
	station_id = models.ForeignKey('station', on_delete=models.CASCADE)
	route_id = models.ForeignKey('route', on_delete=models.CASCADE)
	machine_id = models.ForeignKey('machine', on_delete=models.CASCADE)
	subcity_name = models.ForeignKey('subcity', on_delete=models.CASCADE)
	request_date = models.DateTimeField('date requested')
	def __str__(self):
		return self.station_id+ ' by '+ self.route_id
class assign_vehicle(models.Model):
	route_id = models.ForeignKey('route', on_delete=models.CASCADE)
	vehicle_plate = models.ForeignKey('vehicle', on_delete=models.CASCADE)
	driver_licence  = models.ForeignKey('driver', on_delete=models.CASCADE)
	assign_date = models.DateTimeField('date assigned')
	def __str__(self):
		return self.vehicle_plate+ ' by '+ self.driver_licence