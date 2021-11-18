from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField(max_length=90)
    password = models.CharField(max_length=25)
    cpassword = models.CharField(max_length=25)


choice = (("yes", "Yes"), ("no", "NO"))


class Prediction(models.Model):
    breathingproblem = models.CharField(max_length=3, choices=choice, default=None)
    fever = models.CharField(max_length=3, choices=choice, default=None)
    drycough = models.CharField(max_length=3, choices=choice, default=None)
    sourthroat = models.CharField(max_length=3, choices=choice, default=None)
    runningnose = models.CharField(max_length=3, choices=choice, default=None)
    asthma = models.CharField(max_length=3, choices=choice, default=None)
    lungdisease = models.CharField(max_length=3, choices=choice, default=None)
    headache = models.CharField(max_length=3, choices=choice, default=None)
    heartdisease = models.CharField(max_length=3, choices=choice, default=None)
    diabetes = models.CharField(max_length=3, choices=choice, default=None)
    hypertension = models.CharField(max_length=3, choices=choice, default=None)
    fatigue = models.CharField(max_length=3, choices=choice, default=None)
    gastro = models.CharField(max_length=3, choices=choice, default=None)
    abroadtravel = models.CharField(max_length=3, choices=choice, default=None)
    contact = models.CharField(max_length=3, choices=choice, default=None)
    largergathering = models.CharField(max_length=3, choices=choice, default=None)
    publicplaces = models.CharField(max_length=3, choices=choice, default=None)
    familyworking = models.CharField(max_length=3, choices=choice, default=None)
    wearingmask = models.CharField(max_length=3, choices=choice, default=None)
    sanitization = models.CharField(max_length=3, choices=choice, default=None)
