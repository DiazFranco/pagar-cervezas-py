from django.urls import path
from . import views

urlpatterns = [
    path('status/', views.get_order_status, name='order_status'),
    path('create/', views.create_order, name='create_order'),
]
