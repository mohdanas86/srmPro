from django.urls import path, register_converter, include
from . import views
from . converters import ObjectIdConverter

register_converter(ObjectIdConverter, 'ObjectId')

urlpatterns = [
    path('', views.create_apprisal, name='appraisal'),
    path('hod/<ObjectId:post_id>/', views.update_cumulative, name='update_cumulative'),
    path('apprisal_data/', views.show_apprisal, name='show_apprisal'),
    path('<ObjectId:post_id>/', views.download_pdf, name='download'),
    path('edit/<ObjectId:post_id>/', views.edit_apprisal, name='edit'),
    path('approval/', include('approval.urls')),
]