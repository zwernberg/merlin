from import_export import resources
from merlin.guests.models import HouseHold

class HouseholdResource(resources.ModelResource):
    class Meta:
        model = HouseHold

