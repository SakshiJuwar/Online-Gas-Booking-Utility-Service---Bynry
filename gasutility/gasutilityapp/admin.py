from django.contrib import admin
from gasutilityapp.models import Connections,BookingGass
# Register your models here.

class CoonectionAdmin(admin.ModelAdmin):
    list_display=['id','cname','cemail','cmobile','cgender','cstatus','caadhar','caddress','cpincode','cdob','cdate']
admin.site.register(Connections,CoonectionAdmin)

#class BookingAdmin(admin.ModelAdmin):
    #list_display=['id','name','email','mobile','address','ref','status']
#admin.site.register(Booking,BookingAdmin)
admin.site.register(BookingGass)