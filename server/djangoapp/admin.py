from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Allows one additional blank form for creating CarModel


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'dealer_id', 'car_type', 'year')
    list_filter = ('car_type', 'year')
    search_fields = ('name',)


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]  # Displays CarModel as an inline form within CarMake


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
