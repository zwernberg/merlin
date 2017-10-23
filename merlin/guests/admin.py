from django.contrib import admin
from merlin.guests.models import Guest, HouseHold

# Register your models here.
class guestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tribe', 'attending', 'household')
    list_filter = ('tribe', 'attending')

class GuestInline(admin.TabularInline):
    model = Guest

class HouseHoldAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'family_name', 'address',)
    list_filter = ('family_name',)
    inlines = [
        GuestInline,
    ]

admin.site.register(Guest, guestAdmin)
admin.site.register(HouseHold, HouseHoldAdmin)
