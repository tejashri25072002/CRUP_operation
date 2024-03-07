from django.db import models

# Create your models here.
class Msg(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)
    msg=models.CharField(max_length=200)