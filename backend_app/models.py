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
    password = models.TextField(default="")
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
    
class UploadedTextFile(models.Model):
    fileowner = models.CharField(max_length=255)
    filesender = models.CharField(max_length=255)
    uploaded_text = models.TextField()
    file_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fileowner

class UploadedPdfFile(models.Model):
    fileowner = models.CharField(max_length=255)
    filesender = models.CharField(max_length=255)
    uploaded_pdf = models.TextField()
    file_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fileowner

class Notes(models.Model):
    noteowner = models.CharField(max_length=255)
    title = models.TextField()
    content = models.TextField()
    nodedate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class FormTemplate(models.Model): 
    form_name = models.CharField(max_length=255, default='')
    form_content = models.TextField()

    def __str__(self):
        return self.form_name

class Member(models.Model):
    memberEmail = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    accessnumber = models.CharField(max_length=255)
    member_owner = models.CharField(max_length=255)
    status = models.CharField(max_length = 255, default='Pending')

    
    def __str__(self):
        return self.memberEmail

   



