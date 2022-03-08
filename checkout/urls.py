from django.urls import path
from . import views

from .webhooks import webhook
urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    path('wh/', webhook, name='webhook'),
]
