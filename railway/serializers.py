from rest_framework import serializers
from railway.models import Crew, Station, TrainType, Train, Route, Order, Journey, Ticket


class CrewSerializer(serializers.ModelSerializer):
    # Замість 'route' потрібно вказати 'journeys', щоб показати всі поїздки
    journeys = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="route"
    )

    class Meta:
        model = Crew
        fields = (
            "id",
            "first_name",
            "last_name",
            "journeys"
        )


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = (
            "id",
            "name",
            "latitude",
            "longitude"
        )


class TrainTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainType
        fields = (
            "id",
            "name"
        )


class TrainSerializer(serializers.ModelSerializer):
    train_type = TrainTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = (
            "id",
            "name",
            "cargo_num",
            "places_in_cargo",
            "train_type",
            "image"
        )


class TrainListSerializer(TrainSerializer):
    class Meta:
        model = Train
        fields = (
            "id",
            "name",
            "train_type",
            "image"
        )


class TrainDetailSerializer(TrainSerializer):
    class Meta:
        model = Train
        fields = (
            "id",
            "name",
            "cargo_num",
            "places_in_cargo",
            "train_type",
            "image"
        )


class TrainImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = (
            "id",
            "image"
        )


class RouteSerializer(serializers.ModelSerializer):
    source = serializers.StringRelatedField(queryset=Station.objects.all())
    destination = serializers.StringRelatedField(queryset=Station.objects.all())

    class Meta:
        model = Route
        fields = (
            "id",
            "source",
            "destination",
            "distance"
        )


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "user"
        )
        read_only_fields = ("created_at",)


class JourneySerializer(serializers.ModelSerializer):
    route = RouteSerializer(read_only=True)
    train = TrainSerializer(read_only=True)

    class Meta:
        model = Journey
        fields = (
            "id",
            "route",
            "train",
            "departure_time",
            "arrival_time"
        )


class TicketSerializer(serializers.ModelSerializer):
    journey = JourneySerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "cargo",
            "seat",
            "journey",
            "order"
        )


class TicketListSerializer(serializers.ModelSerializer):
    journey = serializers.StringRelatedField()
    order = serializers.StringRelatedField()

    class Meta:
        model = Ticket
        fields = (
            "id",
            "cargo",
            "seat",
            "journey",
            "order"
        )


class TicketDetailSerializer(serializers.ModelSerializer):
    journey = JourneySerializer(read_only=True)
    order = OrderSerializer(read_only=True)

    class Meta:
        model = Ticket
        fields = (
            "id",
            "cargo",
            "seat",
            "journey",
            "order"
        )
