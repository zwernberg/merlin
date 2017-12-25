from import_export import resources
from merlin.guests.models import HouseHold, Guest

class HouseholdResource(resources.ModelResource):
    class Meta:
        model = HouseHold

class GuestResource(resources.ModelResource):
    class Meta:
        model = Guest

