from django.urls import path
from .import views

urlpatterns = [
    
    path('addmodel/',views.modelcatagory,name='modelname'),
    path('modeldetails/<int:id>',views.cardetails.as_view(),name='modeldetails')

]
