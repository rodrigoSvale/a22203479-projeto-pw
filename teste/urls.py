from django.urls import path
from .views import *


app_name = "teste"

urlpatterns = [
    path('' , index_view , name = 'index'),
    path('outro/', outro_view, name = 'outro')
]