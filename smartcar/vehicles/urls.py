from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from vehicles import views
#from vehicles.views import VehiclesViewSet, UserViewSet, api_root
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^vehicles/$', views.vehicle_list, name='get-vehicle-list'),
    url(r'^vehicles/(?P<pk>[0-9]+)/$', views.vehicle_detail, name='get-vehicle-detail'),
    url(r'^vehicles/(?P<vehicle_pk>[0-9]+)/doors', views.vehicle_security, name='get-vehicle-doors'),
    url(r'^vehicles/(?P<vehicle_pk>[0-9]+)/fuel', views.vehicle_fuel, name='get-vehicle-fuel'),
    url(r'^vehicles/(?P<vehicle_pk>[0-9]+)/battery', views.vehicle_battery, name='get-vehicle-battery'),
    url(r'^vehicles/(?P<vehicle_pk>[0-9]+)/engine', views.vehicle_engine, name='vehicle-engine'),
]

#Using format suffixes gives us URLs that explicitly refer to a given format
#our API will be able to handle URLs as following:
#http://127.0.0.1:8000/vehicles/ Accept:application/json OR http://127.0.0.1:8000/vehicles/ Accept:text/html 
#http://127.0.0.1:8000/vehicles.json OR http://127.0.0.1:8000/vehicles.api
#Do post using format: http --form POST http://127.0.0.1:8000/vehicles/ vin="123" color="white" fourDoorSedan=True twoDoorCoupe=False driveTrain="v9"
urlpatterns = format_suffix_patterns(urlpatterns)

# schema_view = get_schema_view(title='Pastebin API')
# # Create a router and register our viewsets with it.
# router = DefaultRouter()
# #router.register(r'vehicles', views.SnippetViewSet)
# #router.register(r'users', views.UserViewSet)

# urlpatterns = [
#     url(r'^schema/$', schema_view),
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
