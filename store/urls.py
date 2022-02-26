from django.urls import path
from . import views

urlpatterns = [
    path('packs/', views.packs, name='packs'),
    path('<pack_id>/', views.pack_detail, name='pack_detail'),
]
