# pwsite/urls.py

from django.urls import path
from . import views  # importamos views para poder usar as suas funções

app_name = 'novaapp'

urlpatterns = [
    path('historia/', views.historia_view, name='historia'),
    path('index/', views.index_view, name='index'),
    path('sobre/', views.sobre_view, name='sobre'),
]