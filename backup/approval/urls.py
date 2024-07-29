from django.urls import path, register_converter, include
from . import views
from . converters import ObjectIdConverter

register_converter(ObjectIdConverter, 'ObjectId')

urlpatterns =[
    path('<ObjectId:post_id>/', views.data, name='data'),
    path('check/<ObjectId:post_id>/', views.d_data, name='d_data'),
    path('approve/<ObjectId:post_id>/', views.c_approve, name='c_approve')
]