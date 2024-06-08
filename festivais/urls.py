from django.urls import path
from .views import *

app_name = 'festivais'

urlpatterns = [
    path('', index_view, name='index'),
    path('festivais/<int:festival_id>/', festival_detail_view, name='festival_detail'),
]
