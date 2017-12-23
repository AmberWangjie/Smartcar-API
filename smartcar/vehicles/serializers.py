from rest_framework import serializers
from vehicles.models import Vehicle
from vehicles.models import Security
from vehicles.models import Fuel
from vehicles.models import Battery
from vehicles.models import Engine

class VehicleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vehicle
        fields = ('vid', 'vin', 'color', 'doorCount', 'driveTrain')

        
class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('location', 'locked', 'vehicle')

        
class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('percent', 'vehicle')


class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = ('percent', 'vehicle')


#Note for POST request to vehicle_id/engine, the implementation is not an ideal one up to ddl, need to pass the status into requests since I stored the status with its command retrieved from GM beforehand
#should be go to GM every time need to POST to id/engine, then use that info to construct this request
class requestEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('action', 'status', 'vehicle')


class responseEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('status', 'vehicle')




