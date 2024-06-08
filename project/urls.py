"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # incluir include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('noobsite/', include('noobsite.urls')),  # novo path
    path('pwsite/', include('pwsite.urls')),  # novo path
    path('novaapp/', include('novaapp.urls')),  # novo path
    path('bandas/', include('bandas.urls')),  # novo path
    path('artigos/', include('artigos.urls')),  # novo path
    path('curso/', include('curso.urls')),  # novo path
    path('festivais/', include('festivais.urls')),  # novo path
    path('teste/', include('teste.urls')),
    path('meteo/', include('meteo.urls')),
    path('autenticacao/', include('autenticacao.urls')),
    path('', include('Portfolio.urls')),
]