from django.db import models

# Create your models here.
class todo(models.Model):
    number = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    detail = models.TextField()
    tag = models.CharField(max_length=100)
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now=True)
    planDate = models.DateField()
    endDate = models.DateField()
    endYn = models.CharField(max_length=2) 

class tag(models.Model):
    number = models.AutoField(primary_key=True)
    tagname = models.CharField(max_length=100)
    fontcolor = models.CharField(max_length=50)
    bgcolor = models.CharField(max_length=50)
    createDate = models.DateTimeField(auto_now_add=True)
    
    