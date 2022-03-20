from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_admin, name='site_admin'),
    path('add_product/', views.add_product, name='add_product'),
    path('remove_product/', views.remove_product, name='remove_product'),
    path('delete_product/<product_id>', views.delete_product, name='delete_product'),
]
