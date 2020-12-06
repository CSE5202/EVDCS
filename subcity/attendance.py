from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from cityadmin.models import *
from django.db.models import Q,F,Count

from django.contrib import messages 
import datetime

def takeattendance(request):
    trip_no = 0
    raw_driver = vehicle.objects.values('plate_no')
    drivers = [i['plate_no']for i in raw_driver]
    #context1 = {'drivers':drivers}
    #raw_status = AssignVehicle.objects.values('status')
    
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

    return render(request, 'subcity/template/attendance/attendance.html',{'drivers':drivers,'trip_no':trip_no})
def showattendance(request): 
    show = Attendance.objects.all()
    context = {'show': show}
    return render(request, 'subcity/template/attendance/attendance.html', context) 