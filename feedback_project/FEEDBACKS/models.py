from pyexpat import model
from django.db import models

# Create your models here.
class Feedback(models.Model):
    suggestion = models.TextField()
    #name not null
    #suggestion can be null
    #issue can be null