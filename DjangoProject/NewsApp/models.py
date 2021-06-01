from django.db import models

# Create your models here.

class News(models.Model):
    author = models.CharField(default= 'Name', max_length=30)
    title = models.CharField(default= "Title", max_length=30)
    description = models.TextField()


class Sports(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField()










