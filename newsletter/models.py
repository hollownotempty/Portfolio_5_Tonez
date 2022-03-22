import email
from django.db import models

import newsletter

# Create your models here. 

class Subscriber(models.Model):
    """
    Subscriber model for newsletter
    """
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    subject = models.CharField(max_length=250)
    message = models.TextField(max_length=9000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject 