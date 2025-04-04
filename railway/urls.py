from django.urls import include, path
from rest_framework import routers

from railway.views import (
    CrewViewSet,
    TrainTypeViewSet,
    StationViewSet,
    TrainViewSet,
    RouteViewSet,
    OrderViewSet,
    JourneyViewSet,
    TicketViewSet
)

router = routers.DefaultRouter()

router.register("crews", CrewViewSet)
router.register("stations", StationViewSet)
router.register("train-types", TrainTypeViewSet)
router.register("trains", TrainViewSet)
router.register("routes", RouteViewSet)
router.register("orders", OrderViewSet)
router.register("journeys", JourneyViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "railway"
