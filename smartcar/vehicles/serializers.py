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
#        read_only_fields = ('vid','vin')
        
class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('location', 'locked', 'vehicle')
 #       read_only_fields = ('vehicle')
        
class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('percent', 'vehicle')
  #      read_only_fields = ('vehicle')

class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = ('percent', 'vehicle')
   #     read_only_fields = ('vehicle')

class requestEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('action', 'vehicle')
    #    read_only_fields = ('vehicle')
     #   write_only_fields = ('action')

class responseEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('status', 'vehicle')
      #  read_only_fields = ('vehicle')



