from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.dean, name='dean'),
    path('departments/', views.department, name='departments'),
    path('staff detials/<str:department>/', views.show_staff, name='show_staff'),
    path('check/', views.d_approval, name='check'),
    path('approved/', views.d_approved, name='d_approved'),
    path('staff_d/', views.add_staff_d, name='staff_d'),
]