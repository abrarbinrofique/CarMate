from django.shortcuts import render,redirect
from Company.models import companymodel
from Carmodel.models import car


def home(request,company_slug=None):

    data=companymodel.objects.all()
    if company_slug is not None:
      cars=companymodel.objects.get(slug=company_slug)
      choosecar=car.objects.filter(Brandname=cars)
      print(choosecar)
      print(data)

    else:
        choosecar=car.objects.all()
       
    return render(request,'base.html',{'data':data,'car':choosecar})