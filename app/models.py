from operator import mod
from django.db import models

# Create your models here.
class resume_info(models.Model):
    full_name=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    phone=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    about_you=models.TextField(max_length=500)
    education=models.CharField(max_length=200)
    career=models.CharField(max_length=200)
    job1start=models.DateField(default=" ")
    job1end=models.DateField(default=" ")
    job1details=models.TextField(max_length=500, default = " ")
    job2start=models.DateField(default=" ")
    job2end=models.DateField(default=" ")
    job2details=models.TextField(max_length=500, default=" ")
    job3start=models.DateField( default=" ")
    job3end=models.DateField(default=" ")
    job3details=models.TextField(max_length=500,default=" ")
    references=models.TextField(max_length=500)
