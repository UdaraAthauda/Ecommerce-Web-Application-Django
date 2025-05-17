from django.urls import path
from . import views

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),  
    path('process_order/', views.process_order, name="process_order"),  
    path('orders/', views.orders, name="orders"),
]
