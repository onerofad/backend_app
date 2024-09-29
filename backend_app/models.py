from django.db import models
import random

def getRandom():
    random_number = random.randint(1000000000, 9999999999)
    return random_number

class Register(models.Model):
    fname = models.CharField(max_length=255)
    mname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    accessnumber = models.TextField(default=getRandom)
    dob = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fname


