# Create your models here.
# artist_api/models.py
from django.contrib.auth.models import User
from django.db import models

class Work(models.Model):
    LINK_CHOICES = [
        ('YT', 'Youtube'),
        ('IG', 'Instagram'),
        ('OT', 'Other'),
    ]
    
    link = models.CharField(max_length=255)
    work_type = models.CharField(max_length=2, choices=LINK_CHOICES)

class Artist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)
