from django.contrib import admin
from .models import Cars, caravailability 


# Register your models here.
class CarsAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ('category',)

class caravailabilityAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

admin.site.register(Cars,CarsAdmin)
admin.site.register(caravailability,caravailabilityAdmin)



