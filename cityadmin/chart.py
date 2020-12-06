from django.shortcuts import render
from django.db.models import *
from django.http import JsonResponse
from .models import *
import datetime
from datetime import date
from django.contrib.auth.decorators import login_required
def report(request):
    return render(request, 'myapp/template/report/report.html')


def report_chart(request):
    labels = []
    data = []
    label1 = []
    data1 = []
    label2 = []
    data2 = []
    label3 = []
    data3 = []

   
    queryset = waiting_time.objects.all()
    for i in queryset:
      
        x=i.coming_time
        y=i.going_time
        r=str(i.route_id)

        print(x.strftime("%M"))
        w=int(y.strftime("%M"))-int(x.strftime("%M"))
        
  
        labels.append(r)
        data.append(w)
       

    queryset1 = subcity.objects.all()
    for i in queryset1:
        label1.append(i.subcity_name)
        data1.append(i.Number_Of_Station)


    route_query=route.objects.all()
    for x in route_query:
       source=x.source.station_name
       dest=x.destination.station_name
       label=source+" to "+dest
       today = date.today()
       No_assign =  assign_vehicle.objects.filter(assign_date__year=today.year,assign_date__month=today.month,assign_date__day=today.day,source=source,destination=dest).count()
       
       label2.append(label)
       data2.append(No_assign)

    
    
         
    """ queryset2 = subcity.objects.all().order_by('-Number_Of_Station')
    for i in queryset2:
        label2.append(i.subcity_name)
        data2.append(i.Number_Of_Station)"""

    queryset3 = subcity.objects.all()
    for i in queryset3:
        label3.append(i.subcity_name)
        data3.append(i.Number_Of_Station)

    
    
    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'label1': label1,
        'data1': data1,
        'label2': label2,
        'data2': data2,
        'label3': label3,
        'data3': data3,
    })