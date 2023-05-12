# experiences/models.py
from django.db import models


class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
    date_created = models.DateTimeField(auto_now_add=True)
