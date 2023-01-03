from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Teammates

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj1 = Teammates.objects.all()
    return render(request,"index.html",{'result':obj,'results': obj1})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     ans1=x+y
#     ans2=x*y
#     ans3=x-y
#     ans4=x/y
#     return render(request,"result.html",{'a':ans1,'b':ans2,'c':ans3,'d':ans4})
#
