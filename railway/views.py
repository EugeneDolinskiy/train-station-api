from django.shortcuts import render
from rest_framework import viewsets, status, mixins
from railway.models import Crew, Station, Train, Route, Order, Journey, Ticket
from railway.serializers import (
    CrewSerializer,
)
class CrewViewSet(viewsets.ModelViewSet):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer

# Create your views here.
