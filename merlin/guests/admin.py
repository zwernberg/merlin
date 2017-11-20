from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from merlin.guests.models import Guest, HouseHold
from import_export.admin import ImportExportModelAdmin
from merlin.guests.resources import HouseholdResource


# Register your models here.
def make_attending(modeladmin, request, queryset):
    queryset.update(attending='1')

def add_to_wernberg_tribe(modeladmin, request, queryset):
    queryset.update(tribe='0')

def add_to_larson_tribe(modelAdmin, request, queryset):
    queryset.update(tribe='1')



class HasAddressFilter(admin.SimpleListFilter):
    title = _('Has Address')
    parameter_name = 'address__isnull'

    def lookups(self, request, model_admin):
        return (
            ('True', _('No')),
            ('False', _('Yes')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'True':
            return queryset.filter(address__exact='')
        if self.value() == 'False':
            return queryset.filter(address__gt='')

class guestAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'tribe', 'attending', 'household',)
    list_filter = ('tribe', 'attending')
    search_fields = ("first_name", "last_name")
    actions = [
        make_attending,
        add_to_wernberg_tribe,
        add_to_larson_tribe,
        ]

class GuestInline(admin.TabularInline):
    model = Guest
    extra = 1

class HouseHoldAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    resouce_class = HouseholdResource
    search_fields = ("family_name", )
    list_display = ('__str__', 'tribe', 'family_size', 'has_address')
    list_filter = ('tribe', HasAddressFilter)
    inlines = [
        GuestInline,
    ]
    actions = [
        add_to_wernberg_tribe,
        add_to_larson_tribe,
    ]

admin.site.register(Guest, guestAdmin)
admin.site.register(HouseHold, HouseHoldAdmin)
