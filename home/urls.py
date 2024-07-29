from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('aa/', views.s),
    path('apprisal/', include('appraisal.urls'), name='appraisal'),
    path('editprofile/<str:employee_id>', views.edit_profile, name='edit_profile'),
]