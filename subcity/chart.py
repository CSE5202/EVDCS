from django.shortcuts import render
from django.db.models import *
from django.http import JsonResponse
from cityadmin.models import *
import datetime
from django.contrib.auth.decorators import login_required
def report(request):
    return render(request, 'subcity/template/report/report.html')


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
       

    queryset1 = machine.objects.all()
    for i in queryset1:
        label1.append(i.station_id.station_name)
        data1.append(i.id)
       
    queryset2 = subcity.objects.all().order_by('-Number_Of_Station')
    for i in queryset2:
        label2.append(i.subcity_name)
        data2.append(i.Number_Of_Station)

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