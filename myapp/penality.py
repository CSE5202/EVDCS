from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import *
from django.db.models import Q,F,Count

from django.contrib import messages 
import datetime

def takepenality(request): 
    toal_trip = 0
    raw_driver = vehicle.objects.values('plate_no')
    drivers = [i['plate_no']for i in raw_driver]
    #current_date = datetime.now()
    #context1 = {'drivers':drivers}
    #raw_status = AssignVehicle.objects.values('status')
    
    for i in drivers:
        print(i)
        raw_trip = Attendance.objects.filter(driver=i).values('trip_no')
        trip = [k['trip_no']for k in raw_trip]
        print ("trip",  trip)
        for j in trip:
            toal_trip += j
        if toal_trip < 5:
            penalty_status="Punished"
        elif toal_trip <10:
            penalty_status="Warning"
        else:
            penalty_status="good"
        penality = penalty.objects.create(trip_no= toal_trip,penalty_type=penalty_status,vehicle_plate=i)
        penality.save()
    messages.success(request,'successfully Penality is taken')

    return render(request, 'myapp/template/penalty/penality.html',{'trip_no':toal_trip,'penalty_type':penalty_status})
def showpenality(request): 
    show = penalty.objects.all()
    context = {'show': show}
    return render(request, 'myapp/template/penalty/penality.html', context) 
"""       




 
    #return render(request, 'attendance.html', context) 

def takeattendance(request):
    trip_no = 0
    raw_driver = vehicle.objects.values('plate_no')
    drivers = [i['plate_no']for i in raw_driver]
    #context1 = {'drivers':drivers}
    #ra/////////////////w_status = AssignVehicle.objects.values('status')
    
    for i in drivers:
        print(i)
        raw_date = assign_vehicle.objects.filter(vehicles_id__plate_no=i).values('assign_date')
        date = [k['assign_date']for k in raw_date]
        print ("date", date)

        #current_date=date.today()

        #context2 = {'date':date}
        for j in date:
        #if date == current_date:
            q1 = Q(vehicles_id__plate_no=i)
            q2 = Q(status__exact="DONE")
            trip_no = assign_vehicle.objects.filter(q1&q2).count() 
            print("trip_nos: ", trip_no)
            #context={'i': i,'j': j,'trip_no': trip_no}
            #attendance = Attendance.objects.get(driver=i)
        attendance = Attendance.objects.create(driver=i,date=j,trip_no=trip_no)
        attendance.save()
    messages.success(request,'successfully attendance is taken')

    return render(request, 'myapp/template/attendance/attendance.html',{'drivers':drivers,'trip_no':trip_no})
def showattendance(request): 
    show = Attendance.objects.all()
    context = {'show': show}
    return render(request, 'myapp/template/attendance/attendance.html', context) 
"""       