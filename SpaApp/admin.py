from django.contrib import admin
from .models import *


# Register your models here.

class ServiceAdmin(admin.ModelAdmin):
    model = Services
    list_display = ['title', 'description', 'duration', 'price']
    list_display_links = ['title', 'description', 'duration', 'price']

class MastersAdmin(admin.ModelAdmin):
    list_display = ['FIO', 'get_services']

    def get_services(self, obj):
        return ", ".join([str(service) for service in obj.services.all()])

    get_services.short_description = 'Услуги'

class BookingAdmin(admin.ModelAdmin):
    list_display = ['service', 'time_slot', 'client_name', 'masters']
    list_display_links = ['service', 'time_slot', 'client_name', 'masters']


admin.site.register(Masters, MastersAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Services, ServiceAdmin)
