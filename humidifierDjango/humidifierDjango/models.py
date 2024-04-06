from django.db import models

# Create your models here.
class humidity(models.Model):
    humidity_num = models.DecimalField(max_digits= 3, decimal_places = 1)

    def __str__(self):
        return str(self.humidity_num)  
    
class temperature(models.Model):
    temperature_num = models.DecimalField(max_digits= 3, decimal_places = 1)

    def __str__(self):
        return str(self.temperature_num)
    
class airQuality(models.Model):
    quality_num = models.DecimalField(max_digits= 3, decimal_places = 1)

    def __str__(self):
        return str(self.quality_num)
    
class time(models.Model):
    time_create = models.DateField(auto_now_add=True)
    time_update = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.time_update)