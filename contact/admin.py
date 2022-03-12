from django.contrib import admin
from .models import ContactSubmission

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    """
    Admin panel for the contact submissions model
    """
    model = ContactSubmission

    fields = ('user', 'user_email', 'subject', 'message', 'responded_to')

    readonly_fields = ('user', 'user_email')

    order = ('-date',)

admin.site.register(ContactSubmission, ContactAdmin)
