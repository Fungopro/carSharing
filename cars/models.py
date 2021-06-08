from django.db import models
import datetime as dt


class Cars(models.Model):
    car_id = models.PositiveIntegerField(primary_key=True, default=0)
    car_name = models.CharField(max_length=200)
    car_date = models.DateField('Birth date')
    car_number = models.CharField(max_length=10)
    car_status = models.BooleanField(default=False)


class Driver(models.Model):
    driver_id = models.PositiveIntegerField(primary_key=True, default=0)
    driver_name = models.CharField(max_length=200)
    birth_date = models.DateField('Birth date')


class Drive(models.Model):
    drive_id = models.PositiveIntegerField(primary_key=True)
    car = models.ForeignKey(Cars, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    date = models.DateTimeField('Время поездки', default=dt.datetime.now())
    drive_from = models.CharField(max_length=100)
    drive_to = models.CharField(max_length=100, default='')



