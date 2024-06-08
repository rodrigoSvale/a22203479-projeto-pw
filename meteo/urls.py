from django.urls import path
from . import views

app_name = 'meteo'

urlpatterns = [
    path('', views.index, name='index'),
    path('weather_today/', views.weather_today, name='weather_today'),
    path('weather_forecast/', views.weather_forecast, name='weather_forecast'),
    path('cities/', views.cities, name='cities'),  # Nova URL para listar cidades
    path('city_weather_today/<int:city_id>/', views.city_weather_today, name='city_weather_today'),  # Nova URL para previsão do tempo de uma cidade
    path('api/cities/', views.api_cities, name='api_cities'),
    path('api/weather_today/<int:city_id>/', views.api_weather_today, name='api_weather_today'),
    path('api/weather_forecast/<int:city_id>/', views.api_weather_forecast, name='api_weather_forecast'),
]
