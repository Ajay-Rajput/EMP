from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=90)
    phone=models.IntegerField()
    address=models.TextField()

