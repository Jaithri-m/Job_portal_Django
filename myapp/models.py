from django.db import models

# Create your models here.

class Applicant(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(max_length=100)
  position = models.CharField(max_length=100)
  experience = models.PositiveIntegerField()
  status = models.BooleanField(default=False)
  
