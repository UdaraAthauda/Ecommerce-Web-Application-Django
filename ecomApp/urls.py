from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('login/', views.login_user, name="login"),
    path('signup/', views.signup_user, name="signup"),
    path('logout/', views.logout_user, name="logout"),
    path('product/<int:pk>/', views.productDisplay, name="product"),
    path('category/<str:cat>/', views.category, name="category"),
    path('update_user/', views.update_user, name="update_user"),
    path('update_password/', views.update_password, name="update_password"),
]
