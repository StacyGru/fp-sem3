from django.contrib import admin

# Register your models here.

from .models import Driver, CarDetail, Car, Street, AvailableCar

from import_export.admin import ImportExportActionModelAdmin

class DriverAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'gender')
    list_filter = ('gender',)
    search_fields = ('id', 'full_name', 'phone')

class CarDetailAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'gearbox', 'seats', 'engine', 'wheel_side')
    list_filter = ('gearbox', 'engine', 'seats', 'wheel_side')
    search_fields = ('id',)

class CarAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'brand', 'model_name', 'model_details', 'number', 'color')
    list_filter = ('brand', 'model_name', 'color')
    search_fields = ('id', 'model_details', 'number')

class StreetAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'street', 'area')
    list_filter = ('area',)
    search_fields = ('id', 'street')

class AvailableCarAdmin(ImportExportActionModelAdmin):
    list_display = ('id', 'car_id', 'driver', 'street')
    list_filter = ('street',)
    search_fields = ('id', 'car_id', 'driver')

admin.site.register(Driver, DriverAdmin)
admin.site.register(CarDetail, CarDetailAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Street, StreetAdmin)
admin.site.register(AvailableCar, AvailableCarAdmin)