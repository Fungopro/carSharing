from django.contrib import admin

from .models import Driver, Cars, Drive

admin.site.register(Driver)
admin.site.register(Cars)
admin.site.register(Drive)