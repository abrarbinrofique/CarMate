from django.db import models
from Company.models import companymodel
from django.contrib.auth.models import User

# Create your models here.
class car(models.Model):
    Name=models.CharField(max_length=30)
    Price=models.IntegerField()
    Quantity=models.IntegerField()
    Brandname=models.ForeignKey(companymodel,on_delete=models.CASCADE)
    Description=models.TextField()
    user=models.ManyToManyField(User,blank=True,null=True)
    image = models.ImageField(upload_to='post/',blank=True,null=True)


class Purchace(models.Model):
    car=models.ForeignKey(car,on_delete=models.CASCADE,blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Purchace_count=models.IntegerField(blank=True,null=True)



class comments(models.Model):
    carmodel=models.ForeignKey(car, on_delete=models.CASCADE,blank=True,null=True,related_name='comments')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    text=models.TextField()
    createdat=models.DateTimeField(auto_now_add=True)



  
