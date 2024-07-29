from django.urls import path, include, register_converter
from . import views
from . converters import ObjectIdConverter

register_converter(ObjectIdConverter, 'ObjectId')

urlpatterns =[
    path('', views.head, name='head'),
    path('pending/', views.approval, name='approval'),
    path('approved/', views.approved, name='approved'),
    path('staff/', views.staff_data, name='staff'),
    path('delete_staff/<str:employee_id>', views.staff_delete, name='staff_del'),
    path('view Detials/<str:employee_id>', views.view_staff, name="view_staff")
]