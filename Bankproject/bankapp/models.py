from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    cpassword = models.CharField(max_length=250)

    def __str__(self):
        return self.username


class Data(models.Model):
    name = models.CharField(max_length=250)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone = models.IntegerField(max_length=10)
    emailid = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    dbranch = models.CharField(max_length=250)
    accounttype = models.CharField(max_length=250)
    materials = models.CharField(max_length=250)

    def __str__(self):
        return self.name,
