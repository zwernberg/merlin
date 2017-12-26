from django.shortcuts import render
from rest_framework import viewsets
from merlin.invite.serializers import RSVPSerializer, DeclineSerializer
from merlin.invite.models import RSVP, Decline
from rest_framework.permissions import IsAdminUser,AllowAny

# Create your views here.

class RSVPViewSet(viewsets.ModelViewSet):
    queryset = RSVP.objects.all()
    serializer_class = RSVPSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]


    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class DeclineViewSet(viewsets.ModelViewSet):
    queryset = Decline.objects.all()
    serializer_class = DeclineSerializer
    #permission_classes = [IsAccountAdminOrReadOnly]


    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'create':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
