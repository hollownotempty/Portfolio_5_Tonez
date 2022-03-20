from django.urls import path
from . import views

urlpatterns = [
    path('', views.site_admin, name='site_admin'),
    path('add_product/', views.add_product, name='add_product'),
    path('remove_product/', views.remove_product, name='remove_product'),
    path('delete_product/<product_id>', views.delete_product, name='delete_product'),
    path('update_product', views.update_product, name='update_product'),
    path('update_product_detail/<product_id>', views.update_product_detail, name='update_product_detail'),
    path('contact_submissions/', views.contact_submissions, name='contact_submissions'),
    path('contact_submission_detail/<submission_id>', views.contact_submission_detail, name='contact_submission_detail'),
]
