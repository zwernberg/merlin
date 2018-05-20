from rest_framework import serializers
from merlin.invite.models import RSVP, Guest, Decline

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('name', 'food_choice')

class RSVPSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(many=True)
    class Meta:
        model = RSVP
        fields = ('name', 'attending', 'message', 'food_choice', 'song_choice', 'guests')

    def create(self, validated_data):
        guests_data = validated_data.pop('guests')
        rsvp = RSVP.objects.create(**validated_data)
        for guest_data in guests_data:
            Guest.objects.create(rsvp=rsvp, **guest_data)
        return rsvp

class DeclineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Decline
        fields = ('name', 'message')
