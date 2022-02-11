from django.db import models

# Create your models here.


class fish(models.Model):
    fname = models.CharField(max_length=200,null=True,blank=False)
    descpshn = models.TextField(null=True,blank=False)
    img = models.ImageField(upload_to='image',null=True,blank=False)

class pfish(models.Model):
    pname = models.CharField(max_length=200,null=True,blank=False)  
    cate = models.CharField(max_length=200,null=True,blank=False) 
    weight = models.IntegerField(null=True,blank=False) 
    price = models.IntegerField(null=True,blank=False) 
    img = models.ImageField(upload_to='image',null=True,blank=False)

class rfish(models.Model):
    rname = models.CharField(max_length=200,null=True,blank=False)  
    instshn = models.CharField(max_length=200,null=True,blank=False) 
    ingds = models.CharField(max_length=200,null=True,blank=False) 
    img = models.ImageField(upload_to='image',null=True,blank=False)    