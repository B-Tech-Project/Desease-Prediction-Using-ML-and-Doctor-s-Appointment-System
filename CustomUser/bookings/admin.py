from django.contrib import admin
from .models import Booking
# Register your models here.


class BookingAdmin(admin.ModelAdmin):
    list_display = ('patient_email', 'doctor_email', 'time')


admin.site.register(Booking, BookingAdmin)