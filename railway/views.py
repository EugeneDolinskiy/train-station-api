from django.db.models import Count, F
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action as act
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from railway.models import Crew, Station, Train, Route, Order, Journey, Ticket
from railway.serializers import (
    CrewSerializer,
    StationSerializer,
    TrainSerializer,
    TrainListSerializer,
    TrainDetailSerializer,
    TrainImageSerializer,
    RouteSerializer,
    OrderSerializer,
    JourneySerializer,
    TicketSerializer,
    TicketListSerializer,
    TicketDetailSerializer
)


class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


# Create your views here.
