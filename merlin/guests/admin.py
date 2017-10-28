from django.contrib import admin
from merlin.guests.models import Guest, HouseHold

# Register your models here.
def make_attending(modeladmin, request, queryset):
    queryset.update(attending='1')

def add_to_wernberg_tribe(modeladmin, request, queryset):
    queryset.update(tribe='0')

def add_to_larson_tribe(modelAdmin, request, queryset):
    queryset.update(tribe='1')

class guestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tribe', 'attending', 'household',)
    list_filter = ('tribe', 'attending')
    actions = [
        make_attending,
        add_to_wernberg_tribe,
        add_to_larson_tribe,
        ]

class GuestInline(admin.TabularInline):
    model = Guest
    extra = 1

class HouseHoldAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tribe', 'family_size')
    list_filter = ('tribe',)
    inlines = [
        GuestInline,
    ]
    actions = [
        add_to_wernberg_tribe,
        add_to_larson_tribe,
    ]

    # def family_size(self, obj):
    #     return obj.guest_set.count()

admin.site.register(Guest, guestAdmin)
admin.site.register(HouseHold, HouseHoldAdmin)
