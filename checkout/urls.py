from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook'),
]
