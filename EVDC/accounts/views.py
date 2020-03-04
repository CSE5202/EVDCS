
from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages 
from .models import User
def index(request):
   text = """<h1>welcome to my app !</h1>"""
   #return HttpResponse(text)
   return render(request, "myapp/template/login.html", {})
# Create your views here.

# Create your views here.
def hello(request):
   today = datetime.datetime.now().date()
   
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "myapp/template/hello.html", {"today" : today, "days_of_week" : daysOfWeek})
"""def login_view1(request):
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
    return render(request,'accounts/template/login.html', context)
"""
def login_view(request):
  username = request.POST['username']
  password = request.POST['password']
  form=UserLoginForm(request.POST or None)
  user = authenticate(request, username=username, password=password)
  if user is not None:
    login(request, user)
    if user.Roll=='cityAdmin':
      return render(request,'myapp/template/index1.html',{})
    elif user.Roll=='subcityAdmin':
      return render(request,'myapp/template/index1.html',{})
    else:
      return render(request,'myapp/template/main.html',{})
      
  else:
    mes=messages.error(request, "incorrect username and password")
    
    return render(request,'registration/login.html', {})

      # Return an 'invalid login' error message.
     

"""def register(request):
  if request.method == 'POST':
      f = UserCreationForm(request.POST)
      if f.is_valid():
          f.save()
          username = f.cleaned_data.get('username')
          raw_password = f.cleaned_data.get('password1')
          user = authenticate(username=username, password=raw_password)
          login(request, user)
          messages.success(request, 'Account created successfully')
          return redirect('register')

  else:
    f = UserCreationForm()
  return render(request, 'registration/register.html', {'form': f})
"""
def show(request):
  User_list = User.objects.all()
  context = {'User_list': User_list}
  return render(request, 'registration/register_list.html', context)

def edit(request,id):
    User_list = User.objects.get(id=id)
    
    context = {'User_list': User_list }
    return render(request, 'registration/update_user.html', context)
def update(request,id):
    User_list = User.objects.get(id=id)
    
    context = {'User_list': User_list }
    f = UserForm(request.POST,instance=User_list)
    if f.is_valid():
      f.save()
      messages.success(request, 'Account created successfully')
      return redirect('registerList')  
    return render(request, 'registration/update_user.html', context)
def destroy(request,id):
    User_list = User.objects.get(id=id)
    User_list.delete()
    return redirect('registerList')  
def register(request):
  if request.method == 'POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    username=request.POST['username']
    email=request.POST['email'] 
    Roll=request.POST['Roll']
    password=request.POST['password']
    password2=request.POST['password2']


    if password ==password2:
      if User.objects.filter(username=username).exists():
        messages.error(request,'the username is taken')
        return redirect('register')
      else:
        if User.objects.filter(email=email).exists():
          messages.error(request,'the email is being used')
          return redirect('register')
        else:
          user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name,Roll=Roll)
          user.save() 
          messages.success(request,'you are now registered and can log in')
          return redirect('login')
    else:
      messages.error(request,'password do not match')
      return redirect('register')
  else:
    return render(request, 'registration/register.html', {})