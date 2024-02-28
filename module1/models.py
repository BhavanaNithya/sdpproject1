from django.db import models

class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    class Meta:
        db_table='Register'
# Create your models here.

from django.db import models

class Feedbackform(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    feedback_message=models.TextField()

    class Meta:
        db_table = 'Feedbackform'


