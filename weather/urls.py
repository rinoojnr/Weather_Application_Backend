from django.urls import path
from weather import views as weather_views


urlpatterns = [
    path("get_weather_for_loc/<location>/", weather_views.get_weather_data)
]