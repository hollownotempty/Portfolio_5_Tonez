from django.urls import path
from . import views

urlpatterns = [
    path('packs/', views.packs, name='packs'),
]
