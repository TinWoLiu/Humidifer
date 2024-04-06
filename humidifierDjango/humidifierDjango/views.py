from django.shortcuts import render
from django.http import JsonResponse
from .models import humidity, temperature, airQuality, time  # Assuming correct model names

def fetch_data_view(request):
    humidity_data = list(humidity.objects.all().values())
    temperature_data = list(temperature.objects.all().values())
    air_quality_data = list(airQuality.objects.all().values())
    time_data = list(time.objects.all().values())
    
    combined_data = {
        'humidity': humidity_data,
        'temperature': temperature_data,
        'air_quality': air_quality_data,
        'time': time_data,
    }
    
    return JsonResponse(combined_data, safe=False)

def index_view(request):
    # Your code to render the index page
    return render(request, 'index.html')
