import datetime

from django.core import serializers
from django.http import HttpResponse

from cars.models import Cars, Driver, Drive


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def car_data(request, car_id):
    response = "%s."
    return HttpResponse(response % serializers.serialize("json", Cars.objects.order_by('car_id')[car_id:car_id + 1]))


def driver_data(request, driver_id):
    response = "%s."
    return HttpResponse(response % serializers.serialize("json", Driver.objects.order_by('driver_id')[driver_id:driver_id+1]))


def create_drive(request):
    print(request.POST)
    new_drive = Drive(drive_id=request.POST.get('Drive_id', 0),
                      driver_id=request.POST.get('Driver_id', 0),
                      car_id=request.POST.get('Car', 0),
                      date=datetime.datetime.now(),
                      drive_from=request.POST.get('Drive_from', 0),
                      drive_to=request.POST.get('Drive_to', 0))
    new_drive.save()
    return HttpResponse('Drive created')
