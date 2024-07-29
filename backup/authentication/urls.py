from django.urls import path, include
from . import views

urlpatterns = [
    path('home/',include('home.urls'), name='home'),
    path('head/', include('hod.urls')),
    path('dean/', include('dean.urls')),
    path('signup/', views.signup, name='signup'),
    path('otp/', views.otp_verify, name='otp_verify'),
    path('', views.login, name='login'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('forgot_otp_verify/', views.forgot_otp_verify, name='forgot_otp_verify'),
]