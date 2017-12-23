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

    def to_representation(self, obj):
        # get the original representation
        ret = super(VehicleSerializer, self).to_representation(obj)
        ret.pop('vid')
        # here write the logic to check whether `elements` field is to be removed 
        # pop 'elements' from 'ret' if condition is True
        # return the modified representation
        return ret 
        
class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = ('location', 'locked', 'vehicle')

    # def validate(self, data):
    #     """
    #     Check that the 'locked' data is a strict bool type.
    #     """
    #     if data['locked'] in (str(True), str(False), "true", "false"):
    #         raise serializers.ValidationError("Not a strict boolean value")
    #     return data
    
    def to_representation(self, obj):
        # get the original representation
        ret = super(SecuritySerializer, self).to_representation(obj)
        ret.pop('vehicle')
        return ret
        
class FuelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fuel
        fields = ('percent', 'vehicle')

    def to_representation(self, obj):
        # get the original representation
        ret = super(FuelSerializer, self).to_representation(obj)
        ret.pop('vehicle')
        return ret
    
class BatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = Battery
        fields = ('percent', 'vehicle')

    def to_representation(self, obj):
        # get the original representation
        ret = super(BatterySerializer, self).to_representation(obj)
        ret.pop('vehicle')
        return ret

#Note for POST request to vehicle_id/engine, the implementation is not an ideal one up to ddl, need to pass the status into requests since I stored the status with its command retrieved from GM beforehand
#should be go to GM every time need to POST to id/engine, then use that info to construct this request
class requestEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('action', 'status', 'vehicle')


class responseEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = ('action', 'status', 'vehicle')

    def to_representation(self, obj):
	# get the original representation
        ret = super(responseEngineSerializer, self).to_representation(obj)
        ret.pop('vehicle')
        ret.pop('action')
        return ret



