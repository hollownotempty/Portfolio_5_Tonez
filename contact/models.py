from email import message
from django.db import models
from django.conf import settings

# Create your models here.


class ContactSubmission(models.Model):
    """ Model for contact form submission """
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)
    submitted_on = models.DateTimeField(auto_now_add=True)
    responded_to = models.BooleanField(default=False)

    def __str__(self):
        return f'From {self.full_name} on {self.submitted_on}'


class ContactReply(models.Model):
    """
    Replies sent to contact submissions
    """
    submission = models.ForeignKey(ContactSubmission, on_delete=models.CASCADE, blank=True, null=True)
    message = models.TextField(max_length=300, blank=False, null=False)
