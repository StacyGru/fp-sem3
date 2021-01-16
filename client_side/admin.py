from django.contrib import admin

# Register your models here.

from .models import Client, Operator, Order, Ride, DiscountCard

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'gender', 'login', 'password')
    list_filter = ('gender',)
    search_fields = ('id', 'full_name', 'phone', 'login')

class OperatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone', 'gender')
    list_filter = ('gender',)
    search_fields = ('id', 'full_name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'operator', 'order_time', 'status', 'from_place', 'to_place', 'car_class',
                    'driver_gender')
    list_filter = ('operator', 'order_time', 'status', 'car_class', 'driver_gender')
    search_fields = ('id', 'client', 'order_time', 'from_place', 'to_place')

class RideAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'duration', 'mileage', 'price', 'car_id', 'driver')
    list_filter = ('car_id', 'driver')
    search_fields = ('id', 'order', 'duration', 'mileage', 'price')

class DiscountCardAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'points')
    search_fields = ('id', 'client', 'points')

# listeditable чтобы можно было менять значение прям в таблице

admin.site.register(Client, ClientAdmin)
admin.site.register(Operator, OperatorAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Ride, RideAdmin)
admin.site.register(DiscountCard, DiscountCardAdmin)