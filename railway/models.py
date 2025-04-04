import os
import uuid

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.text import slugify
from rest_framework.exceptions import ValidationError


class Crew(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Station(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name


class TrainType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


def train_image_file_path(instance, filename):
    _, extension = os.path.splitext(filename)
    filename = f"{slugify(instance.title)}-{uuid.uuid4()}{extension}"

    return os.path.join("uploads/trains/", filename)


class Train(models.Model):
    name = models.CharField(max_length=255)
    cargo_num = models.IntegerField()
    places_in_cargo = models.IntegerField()
    train_type = models.ForeignKey(
        TrainType,
        on_delete=models.CASCADE,
        related_name="trains"
    )
    image = models.ImageField(
        null=True,
        upload_to=train_image_file_path
    )

    def __str__(self):
        return self.name


class Route(models.Model):
    source = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="departing_routes"
    )
    destination = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="arriving_routes"
    )
    distance = models.FloatField()

    def __str__(self):
        return f"{self.source.name} -> {self.destination.name} ({round(self.distance, 2)})"


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="orders"
    )

    def __str__(self):
        return self.created_at.strftime('%Y-%m-%d %H:%M')


class Journey(models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="journeys"
    )
    train = models.ForeignKey(
        Train,
        on_delete=models.CASCADE,
        related_name="journeys"
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    def clean(self):
        if self.arrival_time <= self.departure_time:
            raise ValidationError("Arrival time must be after departure time.")

    def __str__(self):
        return (
            f"{self.route.source.name} -> {self.route.destination.name} | "
            f"{self.train.name} | {self.departure_time.strftime('%Y-%m-%d %H:%M')} "
            f"– {self.arrival_time.strftime('%Y-%m-%d %H:%M')}"
        )
