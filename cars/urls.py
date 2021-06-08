from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:driver_id>/driver/', views.driver_data, name='driver_id'),
    path('<int:car_id>/car/', views.car_data, name='car_id'),
    path('create_drive/', views.create_drive),
]