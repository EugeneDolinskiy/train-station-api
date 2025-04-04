from rest_framework import serializers

from railway.models import Crew, Station, TrainType, Train


class CrewSerializer(serializers.ModelSerializer):
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
    train_type = TrainTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Train
        fields = (
            "id",
            "name",
            "train_type",
            "image"
        )
