from django.shortcuts import render
import requests


def landing_page(request):
    return render(request, 'Portfolio/landing_page.html')

def about(request):
    return render(request, 'Portfolio/about.html')

def aboutsite(request):
    return render(request, 'Portfolio/aboutsite.html')

def contacto(request):
    return render(request, 'Portfolio/contacto.html')

def projetos(request):
    return render(request, 'Portfolio/projetos.html')

def weather_lisbon(request):
    city_id = 1110600  # ID de Lisboa na API da IPMA
    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    forecast_response = requests.get(forecast_url)
    weather_types_response = requests.get(weather_types_url)

    if forecast_response.status_code == 200 and weather_types_response.status_code == 200:
        forecast_data = forecast_response.json()
        weather_types_data = weather_types_response.json()

        today_forecast = forecast_data['data'][0]
        weather_type_id = today_forecast['idWeatherType']
        weather_description = next(
            (item['descWeatherTypePT'] for item in weather_types_data['data'] if item['idWeatherType'] == weather_type_id),
            'Descrição indisponível'
        )
        weather_icon_url = f"/static/meteo/w_ic_d_{weather_type_id:02d}anim.svg"

        context = {
            'weather_description': weather_description,
            'weather_icon_url': weather_icon_url,
        }
    else:
        context = {
            'weather_description': 'Dados indisponíveis',
            'weather_icon_url': '',
        }

    return render(request, 'Portfolio/layout.html', context)
