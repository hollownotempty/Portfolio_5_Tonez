from django import forms
from .models import Subscriber, Newsletter

class NewsletterForm(forms.ModelForm):
    """
    Form to sign up for newsletter
    """
    class Meta:
        """ Model Form Meta """
        model = Subscriber
        fields = ['email']


class SendNewsletter(forms.ModelForm):
    """
    Form to write and send a new newsletter
    """
    class Meta:
        model = Newsletter
        fields = ['subject', 'message']