from django.db import models
# Create your models here.


class Firm(models.Model):
    firm_name = models.CharField(max_length=40)
    firm_adress = models.CharField(max_length=255)
    firm_email = models.CharField(max_length=100)
    firm_tel = models.CharField(max_length=20)
