from django.db import models

# Create your models here.

GENDER_DRIVER_CHOICES = [
    ('Ж', 'женский'),
    ('М', 'мужской')
]

AREA_STREET_CHOICES = [
    ('центральный', 'центральный'),
    ('северный', 'северный'),
    ('южный', 'южный'),
    ('восточный', 'восточный'),
    ('западный', 'западный')
]

GEARBOX_CARDETAIL_CHOICES = [
    ('автомат', 'автомат'),
    ('механика', 'механика')
]

WHEEL_SIDE_CARDETAIL_CHOICES = [
    ('слева', 'слева'),
    ('справа', 'справа')
]

CHILD_SEAT_CARDETAIL_CHOICES = [
    ('есть', 'есть'),
    ('нет', 'нет')
]

class Driver(models.Model):
    full_name = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=15, choices=GENDER_DRIVER_CHOICES)
    def __str__(self):
        return self.full_name

class CarDetail(models.Model):
    gearbox = models.CharField(max_length=15, choices=GEARBOX_CARDETAIL_CHOICES)
    seats = models.PositiveSmallIntegerField()
    engine = models.PositiveSmallIntegerField()
    wheel_side = models.CharField(max_length=15, choices=WHEEL_SIDE_CARDETAIL_CHOICES)
    child_seat = models.CharField(max_length=15, choices=CHILD_SEAT_CARDETAIL_CHOICES)
    def __str__(self):
        return str(self.id)

class Car(models.Model):
    brand = models.CharField(max_length=150)
    model_name = models.CharField(max_length=150)
    model_details = models.ForeignKey(CarDetail, on_delete=models.CASCADE)
    number = models.CharField(max_length=15)
    color = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)

class Street(models.Model):
    street = models.CharField(max_length=150)
    area = models.CharField(max_length=15, choices=AREA_STREET_CHOICES)
    def __str__(self):
        return self.street

class AvailableCar(models.Model):
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.id)