from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import UserLoginForm
from django.contrib import messages 


def index(request):
   text = """<h1>welcome to my app !</h1>"""
   #return HttpResponse(text)
   return render(request, "myapp/template/login.html", {})
# Create your views here.
def hello(request):
   today = datetime.datetime.now().date()
   
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "myapp/template/hello.html", {"today" : today, "days_of_week" : daysOfWeek})
def login_view(request):
    next=request.GET.get('next')
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        username  = form.cleaned_data.get("username")
        password  = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request,user)
        if next:
            return redirect('/')
    context = {'form':form,}
    return render(request,'myapp/template/login.html', context)
def login_view1(request):
        username  = request.POST["username"]
        password  = request.POST["password"]
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "incorrect username and password")

            return render(request,'myapp/template/login.html')

        if user is not None:
                 login(request,user)
                
              
                 return render(request,'myapp/template/index1.html',{})
        
       
    
