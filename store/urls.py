from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView

urlpatterns = [
    path('', views.store, name='store'),
    path('store/<car_name>', views.car_view, name='car_view'),
    path('checkout/<product_name>', views.checkout, name='checkout'),
    path('profile', views.profile, name='profile'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('checkout/', views.checkout, name='checkout'),
    path('success/<product_name>', views.success, name='success'),
    path('reset_password/', PasswordResetView.as_view(template_name='store/password_reset.html'), name='reset_password'),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name='store/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='store/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name='store/password_reset_done.html'), name='password_reset_complete'),
]