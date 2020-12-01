
from django import forms
from .models import *
from django.contrib.gis.geos import fromstr,Point
class subcityForm(forms.ModelForm):  
	class Meta:  
		model = subcity
		fields = ['subcity_name', 'Number_Of_Station', 'Number_Of_Machine','Number_Of_Root', 'Number_Of_Vehicles']
class stationForm(forms.ModelForm):
 class Meta:  
		model = station
		fields = ['station_name', 'Number_Of_Root', 'location','subcity']

 def save(self, commit=True):
 	self.instance.location = Point(self.cleaned_data["long"], self.cleaned_data["lat"],srid=4326)
 	return super(stationForm, self).save(commit)
class routeForm(forms.ModelForm):  
	class Meta:  
		model = route
		fields = ['route_type', 'length', 'price','source', 'destination']
class vehicleForm(forms.ModelForm):  
	class Meta:  
		model = vehicle
		fields = ['vehicle_name', 'driver', 'plate_no','model', 'subcity','vehicle_size']