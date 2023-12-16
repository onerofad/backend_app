from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    occupation = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    address = models.TextField()
    suite = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    stateorigin = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirmpassword = models.CharField(max_length=255)

    socialsecurity = models.CharField(max_length=255)
    confirmsocialsecurity = models.CharField(max_length=255)
    dob = models.DateField(auto_now_add=True)

    imageurl = models.TextField()
    imageurl1 = models.TextField()
    imageurl2 = models.TextField()

    def __str__(self):
        return self.fname

class Sample(models.Model):
    profileimage = models.TextField()
    cardimagefront = models.TextField()
    carfimageback = models.TextField()

