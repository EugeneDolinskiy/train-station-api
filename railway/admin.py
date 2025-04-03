from django.contrib import admin

from railway.models import Crew, Station, TrainType, Route

admin.site.register(Crew)
admin.site.register(Station)
admin.site.register(TrainType)
admin.site.register(Route)
