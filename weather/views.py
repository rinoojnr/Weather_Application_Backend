import json
import requests

from django.conf import settings
from django.http import HttpResponse, HttpResponseNotFound
def get_weather_data(request, location):
    weather_data_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={settings.WEATHER_API_KEY}&units={"metric"}'
    weather_res = requests.get(weather_data_url)
    if weather_res.status_code == 404:
        return HttpResponseNotFound("Enter a valid city name")
    result = json.loads(weather_res.content)
    weather_desc = {'weather_desc': result.get('weather', [{'description': None}])[0].get('description')}
    response = result['main']
    response.update(weather_desc)
    return HttpResponse(json.dumps(response))