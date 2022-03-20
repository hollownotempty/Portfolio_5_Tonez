from dataclasses import fields
from django import forms
from .models import ContactSubmission, ContactReply


class ContactForm(forms.ModelForm):
    """ Form for the ContactSubmission model """
    class Meta:
        """ Model Form Meta """
        model = ContactSubmission
        fields = ['full_name', 'email', 'subject', 'message']


class ReplyForm(forms.ModelForm):
    """ Form for the ContactSubmission model """
    class Meta:
        """ Model Form Meta """
        model = ContactReply
        fields = ['message',]
