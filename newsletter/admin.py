from django.contrib import admin
from .models import Subscriber, Newsletter

# Register your models here.

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(Subscriber, SubscriberAdmin)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message', 'writer', 'date')
    readonly_fields = [
        "writer",
        "date",
    ]

admin.site.register(Newsletter, NewsletterAdmin)
