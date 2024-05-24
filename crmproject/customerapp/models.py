from django.db import models

# Create your models here.
class Response(models.Model):
    name=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.EmailField(max_length=50)
    responsetype=models.CharField(max_length=10)
    subject=models.CharField(max_length=50)
    responsetext=models.CharField(max_length=10)
    posteddate=models.CharField(max_length=50)
    

class Orders(models.Model):
    productname=models.CharField(max_length=100)
    price=models.IntegerField()
    name=models.CharField(max_length=50)
    contactno=models.CharField(max_length=10)
    emailaddress=models.CharField(max_length=50)
    buydate=models.CharField(max_length=30)
