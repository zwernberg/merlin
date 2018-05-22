from django.contrib import admin
from merlin.invite.models import RSVP, Guest, Decline

# Register your models here.
class GuestAdmin(admin.TabularInline):
    model = Guest
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'attending', 'reserved_count', 'food_choice', 'created')
    list_filter = ('attending',)
    ordering = ['created']
    inlines = [
        GuestAdmin,
    ]
    pass

class DeclineAdmin(admin.ModelAdmin):
    pass

admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Decline, DeclineAdmin)

