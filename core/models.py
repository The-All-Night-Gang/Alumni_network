from email.policy import default
from operator import truediv
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser


class Group(models.Model):
    group_name = models.CharField(max_length=255,null=True)
    
    def __str__(self):
        return self.group_name

class User(AbstractUser):
    i_am = models.ForeignKey(Group,on_delete=models.CASCADE,null=True)
    dob = models.DateField(null=True, blank=True)
    year_of_passing = models.CharField(max_length=20, null=True, blank=True)
    course_studied = models.CharField(max_length=30, null=True, blank=True)
    additional_qualifications = models.TextField(max_length=50, null=True, blank=True)
    present_position_held = models.CharField(max_length=30, null=True, blank=True)
    special_contribution = models.CharField(max_length=30, null=True, blank=True) 
    profile_pic = models.ImageField(upload_to="profile_pic", default="person.svg")

class event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200, null=True)
    event_description = models.TextField(max_length=300, null=True, blank=True)
    event_date = models.DateField()
    Online_link = models.CharField(max_length=300, null=True, blank=True)
    event_location = models.CharField(max_length=200, null=True, blank=True)
    Total_days_of_event = models.IntegerField()

    def _str_(self):
        return self.event_name
