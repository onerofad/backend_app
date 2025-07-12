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

class Owner(models.Model):
    ownername = models.CharField(max_length=255, default='', unique=True)

    def __str__(self):
        return self.ownername

class Tutorial(models.Model):
    title = models.TextField(default='', unique=True)
    image = models.TextField(default='')
    video = models.TextField(default='')
    amount = models.FloatField(default=0)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, to_field='ownername', default='' )

    def __str__(self):
        return self.title
    
class Content(models.Model):
    index = models.IntegerField()
    course_content = models.TextField(default = '')
    sub_content = models.TextField(default = '')
    content_video = models.TextField(default = '')
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, to_field='title', default='')

    def __str__(self):
        return self.course_content

class Alarm(models.Model):
    email = models.CharField(max_length = 255, default='')
    clockTime = models.CharField(max_length = 255, default='')
    aTime = models.CharField(max_length = 255, default='')
    yearformat = models.CharField(max_length = 255, default='')
    dcal = models.CharField(max_length = 255, default='')
    description = models.CharField(max_length = 255, default='')

    def __str__(self):
        return self.description

class CartItems(models.Model):
    tutorial_id = models.IntegerField(default=0)
    emailId = models.CharField(max_length=255, default='')
    item = models.TextField(default='')
    amount = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.item

class Newfolder(models.Model):
    f_name = models.CharField(max_length=255, default='')
    f_owner = models.CharField(max_length=255, default='')
    f_link = models.TextField(default='')

    def __str__(self):
        return self.f_name

class UploadFileToFolder(models.Model):
    folder_id = models.IntegerField(default=0)
    folder_name = models.CharField(max_length=255, default='')
    folder_owner = models.CharField(max_length=255, default='')
    uploaded_link = models.TextField(default='')
    fileName = models.CharField(default='')
    fileSize = models.IntegerField(default=0)
    fileType = models.CharField(max_length=255, default='')
    lastModifiedDate = models.TextField(default='')

    def __str__(self):
        return self.fileName

class MyLearning(models.Model):
    tutorial_id = models.IntegerField(default=0)
    emailId = models.CharField(default='')
#tutorial_name = models.TextField(default='')

    def __str__(self):
        return self.tutorial_name

class Support(models.Model):
    email = models.CharField(max_length=255, default='')
    message = models.TextField(default='')

    def __str__(self):
        return self.message

class TableData(models.Model):
    title = models.CharField(max_length=255, default='')
    emailId = models.CharField(max_length=255, default='')
    head1 = models.CharField(max_length=255, default='')
    head2 = models.CharField(max_length=255, default='')
    head3 = models.CharField(max_length=255, default='')
    head4 = models.CharField(max_length=255, default='')

    value11 = models.CharField(max_length=255, default='')
    value12 = models.CharField(max_length=255, default='')
    value13 = models.CharField(max_length=255, default='')
    value14 = models.CharField(max_length=255, default='')

    value21 = models.CharField(max_length=255, default='data')
    value22 = models.CharField(max_length=255, default='data')
    value23 = models.CharField(max_length=255, default='data')
    value24 = models.CharField(max_length=255, default='data')

    value31 = models.CharField(max_length=255, default='data')
    value32 = models.CharField(max_length=255, default='data')
    value33 = models.CharField(max_length=255, default='data')
    value34 = models.CharField(max_length=255, default='data')

    value41 = models.CharField(max_length=255, default='data')
    value42 = models.CharField(max_length=255, default='data')
    value43 = models.CharField(max_length=255, default='data')
    value44 = models.CharField(max_length=255, default='data')

class Groups(models.Model):
    groupname = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.groupname











