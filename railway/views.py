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


class TrainViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    queryset = Train.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TrainListSerializer
        elif self.action == "retrieve":
            return TrainDetailSerializer
        elif self.action == "upload_image":
            return TrainImageSerializer

        return TrainSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list":
            queryset = queryset.prefetch_related("train_type")

        return queryset

    @act(
        methods=["POST"],
        detail=True,
        permission_classes=[IsAdminUser],
        url_path="upload-image"
    )
    def upload_image(self, request, pk=None):
        train = self.get_object()
        serializer = self.get_serializer(train, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(user=self.request.user)

        if self.action == "list":
            queryset = queryset.prefetch_related("tickets__journey__train")

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class JourneyViewSet(viewsets.ModelViewSet):
    queryset = Journey.objects.all()
    serializer_class = JourneySerializer

    def get_queryset(self):
        return self.queryset.select_related("train", "route")


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TicketListSerializer
        elif self.action == "retrieve":
            return TicketDetailSerializer

        return TicketSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list":
            return queryset.prefetch_related("journey__route", "order")

        return queryset
