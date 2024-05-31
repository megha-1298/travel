from django.http import HttpResponse, request
from django.shortcuts import render
from .models import Place
from .models import Explore

# Create your views here.

def demo(request):
    obj=Place.objects.all()
    exp = Explore.objects.all()
    return render(request,"index.html",{'result':obj,'res':exp})



#def addition(request):
   # x = int(request.GET['num1'])
  #  y = int(request.GET['num2'])
 #   add=x+y
# return render(request,"result.html",{'result':res})

