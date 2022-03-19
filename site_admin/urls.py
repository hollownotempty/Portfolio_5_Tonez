from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_admin, name='site_admin'),
    path('add_product/', views.add_product, name='add_product'),
]
