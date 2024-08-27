from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product_Akshira
# Create your views here.
def home(request):
    obj=Product_Akshira.objects.all()
    return render(request,'index.html',{'obj':obj})