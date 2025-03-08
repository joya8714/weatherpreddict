
import requests
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return render(request, 'weather_app/index.html')

def get_weather(request):
    city = request.GET.get('city')  # Get city from frontend
    if not city:
        return JsonResponse({'error': 'City name is required'}, status=400)

    api_key = "be20b20c4c7cadcc153724d081ee84e0"  # Get API Key from OpenWeatherMap
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
        return JsonResponse(weather_data)
    else:
        return JsonResponse({'error': 'City not found'}, status=404)

