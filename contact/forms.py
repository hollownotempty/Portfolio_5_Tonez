from django import forms
from .models import ContactSubmission


class ContactForm(forms.ModelForm):
    """ Form for the ContactSubmission model """
    class Meta:
        """ Model Form Meta """
        model = ContactSubmission
        fields = '__all__'
