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
    
class UploadedFiles(models.Model):
    fileowner = models.CharField(max_length=255)
    filesender = models.CharField(max_length=255, default='')
    uploaded_file = models.TextField()
    file_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.fileowner
    
class UploadedAudio(models.Model):
    fileowner = models.CharField(max_length=255)
    filesender = models.CharField(max_length=255)
    uploaded_audio = models.TextField()
    file_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fileowner

class UploadedVideo(models.Model):
    fileowner = models.CharField(max_length=255)
    filesender = models.CharField(max_length=255)
    uploaded_video = models.TextField()
    file_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fileowner


