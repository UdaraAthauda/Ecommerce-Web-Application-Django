from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name="view_cart"),
    path('add_to_cart', views.add_to_cart, name="add_to_cart"),
    path('update_cart', views.update_cart, name="update_cart"),
]
