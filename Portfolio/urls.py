from django.urls import path
from .views import landing_page, about, aboutsite, contacto, projetos

app_name = 'Portfolio'

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('about/', about, name='about'),
    path('aboutsite/', aboutsite, name='aboutsite'),
    path('contacto/', contacto, name='contacto'),
    path('projetos/', projetos, name='projetos'),
]
