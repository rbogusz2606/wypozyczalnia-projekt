from django.urls import reverse
from django.db import models




# Create your models here.

class Cars(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    fuel = models.CharField(max_length=30)
    engine_capacity = models.FloatField(default=0.0)
    door_number = models.IntegerField(default= 0)
    fuel_consumption_per_100km = models.CharField(max_length=50)
    number_of_airbags = models.IntegerField()
    description = models.CharField(default=None, max_length=100000)
    image = models.ImageField(default= None, blank=True, null=True, upload_to='images/fotki')

    class Meta:
        verbose_name_plural = "Cars"
        
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("car-detail", args=[self.id])
    
class caravailability(models.Model):
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    car_select = models.ForeignKey(Cars, on_delete=models.CASCADE, default= None)
    class Meta:
        verbose_name_plural = "caravailability"

    
