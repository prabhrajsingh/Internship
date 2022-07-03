from pyexpat import model
from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save, post_save
from django.urls import reverse


# Create your models here.
class Feedback(models.Model):
    suggestion = models.TextField()
    timestamp = models.DateTimeField(auto_now_add = True) 
    updated = models.DateTimeField(auto_now = True)
    
