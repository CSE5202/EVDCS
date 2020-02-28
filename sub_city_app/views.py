from django.shortcuts import render
from django.http import HttpResponse

posts=[
   {'name':'taxi1',
    'plate_no':'AA546789',
    'driver':'Leul Biyaz',
    'type':'1',
    'model':'gada12'},
    {'name':'taxi2',
    'plate_no':'AA98076',
    'driver':'Tola kuma',
    'type':'1',
    'model':'gada12'}
]


def home(request):
	context={
	 'posts':posts,
     'title':'Subcity - Home'
	}
	return render(request,'sub_city_app/home.html',context)

def register_driver(request):
	return render(request,'sub_city_app/register_driver.html',{'title': 'register_driver'})

