from django.contrib import admin
from .models import Departments,Doctors,Booking
# Register your models here.

admin.site.register(Departments)
admin.site.register(Doctors)


class BookingAdmin(admin.ModelAdmin):

    list_display = ('id','full_name','email','date','p_number','doc_name','booked_on')

admin.site.register(Booking,BookingAdmin)