from django.db import models

# Create your models here.
class Message(models.Model):
    date = models.DateTimeField()
    sender = models.TextField()
    text = models.TextField()
    