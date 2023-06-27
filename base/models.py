from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    admission_number= models.IntegerField(null=True)
    dob = models.DateField(null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    BATCH_CHOICES = (
        ('B22ECA', 'B22ECA'),
        ('B22ECB', 'B22ECB'),
        ('Default','Default'),
    )
    ROLES = (
        ('S', 'Student'),
        ('A', 'Advisor'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="M")
    batch = models.CharField(max_length=7,choices=BATCH_CHOICES,default="Default")
    role = models.CharField(max_length=7,choices=ROLES,default="S")
    phone_no=models.CharField(null=True,blank=True,max_length=20);
    guardian=models.CharField(max_length=40,null=True,blank=True);
    guardian_no=models.CharField(null=True,blank=True,max_length=20);
    teacher_remarks=models.CharField(null=True,blank=True,max_length=200);
    # add additional fields in here

    def __str__(self):
        return self.username
    

class Activity(models.Model):
        name=models.CharField(max_length=100)
        date=models.CharField(max_length=50)
