from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
   text = """<h1>welcome to my app !</h1>"""
   #return HttpResponse(text)
   return render(request, "myapp/template/login.html", {})
# Create your views here.
def register(request):
   text = """<h1>welcome to my app !</h1>"""
   #return HttpResponse(text)
   return render(request, "registration/register.html", {})
# Create your views here.
