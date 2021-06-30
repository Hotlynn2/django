from django.db import models

# Create your models here.

class News(models.Model):
    author = models.CharField(default= 'Name', max_length=30)
    title = models.CharField(default= "Title", max_length=30) 
    description = models.TextField()

    def __str__(self):
        return self.author


class Sports(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.author


class RegistrationData(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)



 






