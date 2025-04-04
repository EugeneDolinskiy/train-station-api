from django.contrib import admin

from railway.models import Crew, Station, TrainType, Route, Train, Order, Journey

admin.site.register(Crew)
admin.site.register(Station)
admin.site.register(TrainType)
admin.site.register(Route)
admin.site.register(Train)
admin.site.register(Order)
admin.site.register(Journey)
