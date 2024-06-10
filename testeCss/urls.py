from django.urls import path
from .views import *

app_name = 'testeCss'

urlpatterns = [
    path('', pagina_view, name='testeCss'),
]
