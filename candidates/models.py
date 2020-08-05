from django.db import models
import numpy as np
from django.contrib.auth.models import User

# Create your models here.

class Candidate(models.Model):
    candidate_id = models.CharField(max_length = 128)
    name = models.CharField(max_length = 128)
    #user_name = models.ForeignKey(User, on_delete=models.CASCADE) # 1対多対応
    address_number = models.CharField(max_length = 128)
    address = models.CharField(max_length = 128)
    year = models.CharField(max_length = 32)
    month = models.CharField(max_length = 32)
    day = models.CharField(max_length = 32)
    univ = models.CharField(max_length = 128)
    department = models.CharField(max_length = 128)
    course = models.CharField(max_length = 128)
    enroll_date = models.CharField(max_length = 128)
    graduate_date = models.CharField(max_length = 128)
    carrer_vision = models.ImageField(upload_to='carrer_vision', default = None, null = True, blank = True)
    output = models.ImageField(upload_to='output', default = None, null = True, blank = True)

    def __str__(self):
        return self.name
