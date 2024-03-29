from django.contrib import admin
from humidifierDjango.models import humidity, temperature, airQuality, time
# Register your models here.
admin.site.register(humidity)
admin.site.register(temperature)
admin.site.register(airQuality)
admin.site.register(time)