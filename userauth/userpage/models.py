from django.db import models

# Create your models here.
class Singin(models.Model):
    username=models.CharField(max_length=20)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=10)
    date=models.DateField()


    def __str__(self):
        return self.username
    
    