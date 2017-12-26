from django.contrib import admin
from merlin.invite.models import RSVP, Decline

# Register your models here.

class RSVPAdmin(admin.ModelAdmin):
    pass

class DeclineAdmin(admin.ModelAdmin):
    pass

admin.site.register(RSVP, RSVPAdmin)
admin.site.register(Decline, DeclineAdmin)

