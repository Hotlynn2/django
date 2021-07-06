from django.db import models


class News(models.Models):
    author = models.CharField(max_length = 30),
    title = models.CharField(max_length = 30),
    description = models.TextField(max_length = 70)








