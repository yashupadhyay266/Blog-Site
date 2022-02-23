from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Task(models.Model):
    taskuser=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    task_id=models.IntegerField(default=0)
    tasktitle=models.CharField(max_length=200)
    taskdescription=models.TextField()
    added_time=models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.tasktitle 

class ImageFromUser(models.Model):
    imageuser=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    date_uploaded=models.DateField(auto_now=True)
    caption=models.CharField(max_length=200)
    imagedescription=models.TextField(max_length=254)
    image_uploaded=models.ImageField(upload_to='images',null=True)
    def __str__(self):
        return str(self.id)
    
   