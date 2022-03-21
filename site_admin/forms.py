from django import forms
from store.models import Packs

class AddProductForm(forms.ModelForm):
    """ Form for the ContactSubmission model """
    class Meta:
        """ Model Form Meta """
        model = Packs
        fields = ['name', 'category', 'price', 'description', 'image', 'download_link', 'demo_link', 'stripe_price_id']