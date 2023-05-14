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
    phone_no=models.CharField(null=True);
    guardian=models.CharField(max_length=40,null=True);
    guardian_no=models.CharField(null=True);
    teacher_remarks=models.CharField(null=True);
    # add additional fields in here

    def __str__(self):
        return self.username