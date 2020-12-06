from django.shortcuts import render
from .models import *
from random import sample
from datetime import datetime
from django.contrib.auth.decorators import login_required
def deploy(request):
    #last_round = 0
    raw_last_round = deployment.objects.values('rounde').last()
    print("raw_last_round: ", raw_last_round)
    if raw_last_round != None:
        last_round = raw_last_round['rounde']
    else:
        last_round = 0    
    print("last_round: ", last_round)

    raw_subcities = subcity.objects.values('id')
    subcities = [i['id'] for i in raw_subcities]
    print("subcities: ", subcities)

    #the real deal
    for i in subcities:
        print("subcity: ",i)
        raw_vehicles = vehicle.objects.filter(subcity = i).values('id')
        vehicles = [i['id'] for i in raw_vehicles]  
        print ("vehicles in subcity: ", vehicles)

        raw_route_types_in_subcity = station.objects.values('source__route_type').filter(subcity = i).exclude(source__route_type = None) 
        route_types_in_subcity = [i['source__route_type'] for i in raw_route_types_in_subcity]

        print("route_types_in_subcity: ", route_types_in_subcity)

        no_of_route_types_in_subcity = len(route_types_in_subcity)
        try:
            no_of_recent_deployments_in_subcity  = last_round  % no_of_route_types_in_subcity

        except:
            no_of_recent_deployments_in_subcity  = 0

        print("no_of_recent_deployments_in_subcity: ", no_of_recent_deployments_in_subcity)
        for j in vehicles:
            print("vehicle: ", j)
            raw_recent_route_types = route.objects.filter(deployment__vehicle_plate = j, deployment__rounde__gte = (last_round - no_of_recent_deployments_in_subcity + 1) ).values('route_type')
            recent_route_types = [i['route_type'] for i in raw_recent_route_types]
            print("recent route types: ", recent_route_types)

            
            valid_route_types = list(set(route_types_in_subcity) - set(recent_route_types))    
            print("valid_route_types: ", valid_route_types)   
            
            if len(valid_route_types) > 0:

                random_route_type = sample(valid_route_types, 1)
                print("random_route_type: ", random_route_type)

                
                raw_valid_routes = station.objects.filter(source__route_type = random_route_type[0], subcity = i).values("source__id")
                valid_routes = [i['source__id'] for i in raw_valid_routes]
                print("valid routes:::: ", valid_routes)
            
                random_route = sample(valid_routes, 1)
                print("random route: ", random_route)

                
                current_route = route.objects.filter(id = random_route[0]).get()
                vehicle_plate_no =vehicle.objects.filter(id = j) .get()
                current_time = datetime.now()

                source_name = station.objects.filter(source__id = random_route[0]).values("station_name")
                destination_name = station.objects.filter(dest__id = random_route[0]).values("station_name")
                route_type = current_route.route_type
                route_length = current_route.length
                route_price = current_route.price


                new_deployment = deployment(route_id = current_route, vehicle_plate = vehicle_plate_no, rounde = last_round + 1, reg_date = current_time, source_name = source_name, deestination_name = destination_name, route_type = route_type,  route_price = route_price, route_length = route_length)
                new_deployment.save()
     

                deployments = deployment.objects.all()
                render(request,'myapp/template/deploy/deployment.html', {'deployments': deployments})

                

    current_round = last_round + 1        


           
                      
            

    current_deployment = deployment.objects.filter(rounde = current_round).all()
    past_deployments = deployment.objects.filter(rounde__lte = last_round).all().order_by('-rounde')
    deployments = deployment.objects.all()
            

    return render(request,'myapp/template/deploy/deployment.html', {'current_deployment': current_deployment, 'past_deployments': past_deployments})





def genarate_id(modelName):
    last_id = modelName.objects.values("new_id").last()
    if last_id == None :
        new_id = modelName__class__.__name__

        
        currentYear = datetime.now().year 
        new_id = new_id +"/0001/" + str(currentYear)
    else:    
        splitted_id = last_id.split("/")
        new_id = splitted_id[0] + "/"
        mid_id = int(splitted_id[1]) + 1
        no_of_zeros = 4 - len(str(mid_id))

        for i in range(0, no_of_zeros):
            mid_id = "0" + mid_id

        currentYear = datetime.now().year 
        new_id = new_id + mid_id + "/" + str(currentYear)

    return new_id    

def check_generate_id():
    check_generate_id()

    


