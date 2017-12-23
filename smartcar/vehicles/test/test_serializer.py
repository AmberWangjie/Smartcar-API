from django.test import TestCase
import json
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from vehicles.models import Vehicle
from vehicles.models import Security
from vehicles.models import Fuel
from vehicles.models import Battery
from vehicles.models import Engine
from vehicles.serializers import VehicleSerializer
from vehicles.serializers import SecuritySerializer
from vehicles.serializers import FuelSerializer
from vehicles.serializers import BatterySerializer
from vehicles.serializers import requestEngineSerializer
from vehicles.serializers import responseEngineSerializer

class vehicleSerializerTest(TestCase):
    """ Test module for vehicle serializer"""
    def setUp(self):
        self.object_attributes = {'vid': '1234', 'vin':'1213231', 'color':'Metallic Silver', 'doorCount':4, 'driveTrain':'v8'}
        self.serializer_data = {'vid': '1235', 'vin':'1235AZ91XP', 'color':'Forest Green', 'doorCount':2, 'driveTrain':'electric'}
        self.vehicle = Vehicle.objects.create(**self.object_attributes)
        self.serializer = VehicleSerializer(instance=self.vehicle)


    def test_contain_field_vehicle(self):
        """ verify if the serialzier has the exact attributes it is expected to"""
        data = self.serializer.data
        #using set to make sure addition or removal of any field to the serializer will be detected by test
       # print(set(data.keys()))
        self.assertEqual(set(data.keys()), set(['vin', 'color', 'doorCount', 'driveTrain']))

        """ check if serialzier produces expected data to single field"""
        self.assertEqual(data['color'], self.object_attributes['color'])
        self.assertEqual(data['doorCount'], self.object_attributes['doorCount'])


    def test_invalid_field_vehicle(self):
        """verify if the serialzier has the ability to detect invalid field """
       # data = self.serializer.data
        invalid_list = [3, 4.0]
        for item in invalid_list:
            self.serializer_data['doorCount'] = item
            serializer = VehicleSerializer(data = self.serializer_data)
            self.assertFalse(serializer.is_valid())
        self.assertEqual(set(serializer.errors), set(['doorCount']))


class securitySerializerTest(TestCase):
    """ Test module for security serializer"""
    def setUp(self):
        self.vehicle_attributes = {'vid': '1234', 'vin':'1213231', 'color':'Metallic Silver', 'doorCount':4, 'driveTrain':'v8'}
        self.object_attributes = {'location': "frontLeft", 'locked': True, 'vehicle':'1234'}
        self.serializer_data = {'location': "frontRight", 'locked': False, 'vehicle':'1234'}
        self.vehicle = Vehicle.objects.create(**self.vehicle_attributes)
        self.security = self.vehicle.doors.create(**self.object_attributes)
        self.serializer = SecuritySerializer(instance=self.security)

    def test_contain_field_security(self):
        """ verify if the serialzier has the exact attributes it is expected to"""
        data = self.serializer.data
        #using set to make sure addition or removal of any field to the serializer will be detected by test
        self.assertEqual(set(data.keys()), set(['location', 'locked']))
        
        """ check if serialzier produces expected data to single field"""
        self.assertEqual(data['location'], self.object_attributes['location'])
        self.assertEqual(data['locked'], self.object_attributes['locked'])

    # def test_invalid_field_security(self):
    #    # data = self.serializer.data
    #     invalid_list = [str(True)]
    #     for item in invalid_list:
    #         self.serializer_data['locked'] = item
    #         serializer = SecuritySerializer(data = self.serializer_data)
    #         self.assertFalse(serializer.is_valid())
    #     self.assertEqual(set(serializer.errors), set(['locked']))

class energySerializerTest(TestCase):
    """ Test module for serializer of energy object (fuel/battery)"""
    def setUp(self):
        self.vehicle_attributes = {'vid': '1234', 'vin':'1213231', 'color':'Metallic Silver', 'doorCount':4, 'driveTrain':'v8'}
        self.object_attributes = {'percent': 35.6, 'vehicle':'1234'}
        self.serializer_data = {'percent': 1.37, 'vehicle':'1234'}
        self.vehicle = Vehicle.objects.create(**self.vehicle_attributes)
        self.fuel = self.vehicle.fuelLevel.create(**self.object_attributes)
        self.serializer = FuelSerializer(instance=self.fuel)

    def test_contain_field_energy(self):
        """ verify if the serialzier has the exact attributes it is expected to"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['percent']))
        """ check if serialzier produces expected data to single field"""
        self.assertEqual(data['percent'], self.object_attributes['percent'])

    # def test_invalid_field_energy(self):
    #     """verify if the serialzier has the ability to detect invalid field """
    #     invalid_list = [int(40.0), "null"]
    #     for item in invalid_list:
    #         self.serializer_data['percent'] = item
    #         serializer = FuelSerializer(data=self.serializer_data)
    #         self.assertFalse(serializer.is_valid())
    #     self.assertEqual(set(serializer.errors), set(['percent']))
