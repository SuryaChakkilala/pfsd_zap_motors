from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('store/<car_name>', views.car_view, name='car_view'),
    path('checkout/<product_name>', views.checkout, name='checkout'),
    path('profile', views.profile, name='profile'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
]