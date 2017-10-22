from django.contrib import admin
from merlin.guests.models import Guest

# Register your models here.
class guestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tribe', 'attending',)
    list_filter = ('tribe', 'attending')

admin.site.register(Guest, guestAdmin)
