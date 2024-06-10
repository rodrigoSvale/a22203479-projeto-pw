from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    if response.status_code == 200:
        cities_data = response.json()
        cities = cities_data['data']
    else:
        cities = []

    context = {
        'cities': cities,
    }

    return render(request, 'meteo/index.html', context)

def weather_today(request):
    weather_url = 'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/1110600.json'
    weather_response = requests.get(weather_url)

    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
    weather_types_response = requests.get(weather_types_url)

    if weather_response.status_code == 200 and weather_types_response.status_code == 200:
        weather_data = weather_response.json()
        weather_types_data = weather_types_response.json()

        today_forecast = weather_data['data'][0]
        weather_type_id = today_forecast['idWeatherType']

        weather_description = next(
            (item['descWeatherTypePT'] for item in weather_types_data['data'] if item['idWeatherType'] == weather_type_id),
            'Descrição indisponível'
        )

        context = {
            'city': 'Lisboa',
            'min_temp': today_forecast['tMin'],
            'max_temp': today_forecast['tMax'],
            'date': today_forecast['forecastDate'],
            'weather_description': weather_description,
            'precipitation': today_forecast['precipitaProb'],
            'icon_url': f"/static/meteo/w_ic_d_{weather_type_id:02d}anim.svg",
        }
    else:
        context = {'error': 'Could not retrieve weather data'}

    return render(request, 'meteo/weather_today.html', context)

def city_weather_today(request, city_id):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    cities_response = requests.get(cities_url)
    if cities_response.status_code == 200:
        cities_data = cities_response.json()
        city_name = next((city['local'] for city in cities_data['data'] if city['globalIdLocal'] == city_id), 'Unknown')
    else:
        city_name = 'Unknown'

    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'

    response = requests.get(forecast_url)
    weather_types_response = requests.get(weather_types_url)

    if response.status_code == 200 and weather_types_response.status_code == 200:
        forecast_data = response.json()
        weather_types_data = weather_types_response.json()
        today_forecast = forecast_data['data'][0]

        weather_type_id = today_forecast['idWeatherType']
        weather_description = next(
            (item['descWeatherTypePT'] for item in weather_types_data['data'] if item['idWeatherType'] == weather_type_id),
            'Descrição indisponível'
        )

        context = {
            'city': city_name,
            'min_temp': today_forecast['tMin'],
            'max_temp': today_forecast['tMax'],
            'date': today_forecast['forecastDate'],
            'weather_description': weather_description,
            'precipitation': today_forecast['precipitaProb'],
            'icon_url': f"/static/meteo/w_ic_d_{weather_type_id:02d}anim.svg",
        }
    else:
        context = {'error': 'Could not retrieve weather data'}

    return render(request, 'meteo/weather_today.html', context)

def weather_forecast(request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    cities_data = response.json()

    cities = cities_data['data']

    selected_city = request.GET.get('city', 'Lisboa')
    selected_city_id = next((city['globalIdLocal'] for city in cities if city['local'] == selected_city), None)

    if selected_city_id:
        forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{selected_city_id}.json'
        response = requests.get(forecast_url)
        if response.status_code == 200:
            forecast_data = response.json()
            weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
            weather_types_response = requests.get(weather_types_url)
            weather_types_data = weather_types_response.json()

            forecast = []
            for day_forecast in forecast_data['data'][:5]:
                weather_type_id = day_forecast['idWeatherType']
                weather_description = next(
                    (item['descWeatherTypePT'] for item in weather_types_data['data'] if item['idWeatherType'] == weather_type_id),
                    'Descrição indisponível'
                )
                forecast.append({
                    'date': day_forecast['forecastDate'],
                    'min_temp': day_forecast['tMin'],
                    'max_temp': day_forecast['tMax'],
                    'weather_description': weather_description,
                    'precipitation': day_forecast['precipitaProb'],
                    'icon_url': f"/static/meteo/w_ic_d_{weather_type_id:02d}anim.svg",
                })
        else:
            forecast = []
    else:
        forecast = []

    context = {
        'cities': cities,
        'forecast': forecast,
        'selected_city': selected_city,
    }

    return render(request, 'meteo/weather_forecast.html', context)

def cities(request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    if response.status_code == 200:
        cities_data = response.json()
        cities = cities_data['data']
    else:
        cities = []

    context = {
        'cities': cities,
    }

    return render(request, 'meteo/cities.html', context)

def api_cities(request):
    cities_url = 'https://api.ipma.pt/open-data/distrits-islands.json'
    response = requests.get(cities_url)
    if response.status_code == 200:
        cities_data = response.json()
        return JsonResponse(cities_data['data'], safe=False)
    else:
        return JsonResponse({'error': 'Could not retrieve cities data'}, status=500)

def api_weather_today(request, city_id):
    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(forecast_url)
    if response.status_code == 200:
        forecast_data = response.json()
        today_forecast = forecast_data['data'][0]
        weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
        weather_types_response = requests.get(weather_types_url)
        weather_types_data = weather_types_response.json()
        weather_type_id = today_forecast['idWeatherType']
        weather_description = next(
            (item['descWeatherTypePT'] for item in weather_types_data['data'] if item['idWeatherType'] == weather_type_id),
            'Descrição indisponível'
        )
        result = {
            'city': city_id,
            'min_temp': today_forecast['tMin'],
            'max_temp': today_forecast['tMax'],
            'date': today_forecast['forecastDate'],
            'weather_description': weather_description,
            'precipitation': today_forecast['precipitaProb'],
            'icon_url': f"https://api.ipma.pt/icons/w_ic_d_{weather_type_id:02d}.svg",
        }
        return JsonResponse(result)
    else:
        return JsonResponse({'error': 'Could not retrieve weather data'}, status=500)

def api_weather_forecast(request, city_id):
    forecast_url = f'https://api.ipma.pt/open-data/forecast/meteorology/cities/daily/{city_id}.json'
    response = requests.get(forecast_url)
    if response.status_code == 200:
        forecast_data = response.json()
        weather_types_url = 'https://api.ipma.pt/open-data/weather-type-classe.json'
        weather_types_response = requests.get(weather_types_url)
        weather_types_data = weather_types_response.json()

        forecast = []
        for day_forecast in forecast_data['data'][:5]:
            weather_type_id = day_forecast['idWeatherType']
            weather_description = next(
                (item['descWeatherTypePT'] for item in weather_types_data['data'] if item['idWeatherType'] == weather_type_id),
                'Descrição indisponível'
            )
            forecast.append({
                'date': day_forecast['forecastDate'],
                'min_temp': day_forecast['tMin'],
                'max_temp': day_forecast['tMax'],
                'weather_description': weather_description,
                'precipitation': day_forecast['precipitaProb'],
                'icon_url': f"https://api.ipma.pt/icons/w_ic_d_{weather_type_id:02d}.svg",
            })
        return JsonResponse(forecast, safe=False)
    else:
        return JsonResponse({'error': 'Could not retrieve weather data'}, status=500)