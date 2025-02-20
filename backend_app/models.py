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
    verifyemail = models.IntegerField(default = 0)
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

class Community(models.Model):
    communityname = models.CharField(max_length=255, unique=True)
    role = models.CharField(max_length=255)
    community_owner = models.CharField(max_length=255)

    def __str__(self):
        return self.communityname

class Member(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, to_field='communityname')
    memberEmail  = models.CharField(max_length=255)
    memberRole = models.CharField(max_length=255)
    accessnumber = models.CharField(max_length=255, default=getRandom)
    status = models.CharField(max_length =255, default='pending')
    community_owner = models.CharField(max_length=255, default="")
    
    def __str__(self):
        return self.memberEmail

class CourseWebUser(models.Model):
    email = models.CharField(max_length = 255, default='')
    password = models.CharField(max_length = 255, default='')
    firstname = models.CharField(max_length = 255, default='')
    lastname = models.CharField(max_length = 255, default='')
    phone = models.CharField(max_length = 255, default='')


    def __str__(self):
        return self.firstname

class Tutor(models.Model):
    tutorname = models.CharField(max_length=255, default='', unique=True)

    def __str__(self):
        return self.tutorname
    
class CourseDetails(models.Model):
    description = models.TextField(default='', unique=True)

    def __str__(self):
        return self.description

class CourseContent(models.Model):
    index = models.IntegerField()
    course_title = models.TextField(default = '', unique=True)
    subtitle = models.TextField(default = '')
    video = models.TextField(default = '')

    def __str__(self):
        return self.course_title

class Course(models.Model):
    title = models.TextField(default='')
    image = models.TextField(default='')
    video = models.TextField(default='')
    amount = models.FloatField(default=0)
    coursedetails = models.ForeignKey(CourseDetails, on_delete=models.CASCADE, to_field='description')
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, to_field='tutorname', default='' )
    coursecontent = models.ForeignKey(CourseContent, on_delete=models.CASCADE, to_field='course_title', default='')

    def __str__(self):
        return self.title

class Alarm(models.Model):
    email = models.CharField(max_length = 255, default='')
    clockTime = models.CharField(max_length = 255, default='')
    aTime = models.CharField(max_length = 255, default='')
    yearformat = models.CharField(max_length = 255, default='')
    dcal = models.CharField(max_length = 255, default='')
    description = models.CharField(max_length = 255, default='')

    def __str__(self):
        return self.description



