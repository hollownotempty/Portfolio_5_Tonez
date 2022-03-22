from django import forms
from .models import Subscriber

class NewsletterForm(forms.ModelForm):
    """
    Form to sign up for newsletter
    """
    class Meta:
        """ Model Form Meta """
        model = Subscriber
        fields = ['email']