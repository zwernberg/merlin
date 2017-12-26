from rest_framework import serializers
from merlin.invite.models import RSVP, Decline


class RSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSVP
        fields = ('name', 'attending', 'message')

class DeclineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decline
        fields = ('name', 'message')
