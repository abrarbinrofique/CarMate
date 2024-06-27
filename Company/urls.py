
from django.urls import path
from .import views

urlpatterns = [
    
    path('addcompany/',views.companycatagory,name='companyname')

]
