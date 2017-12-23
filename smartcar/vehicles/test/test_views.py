from django.test import TestCase
import json
import requests
from rest_framework import status
from django.test import Client
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


# initialize the APIClient app
client = Client()

class GetAllVehiclesTest(TestCase):
    """ Test module for GET all vehicles API """

    def setUp(self):
        Vehicle.objects.create(
            vid='1234', vin='1213231', color='Metallic Silver', doorCount=4, driveTrain='v8')
        Vehicle.objects.create(
            vid='1235', vin='1235AZ91XP', color='Forest Green', doorCount=2, driveTrain='electric')
       

    def test_get_all_vehicles(self):
        # get API response
        response = client.get(reverse('get-vehicle-list'))
        # get data from db
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleVehicleTest(TestCase):
    """ Test module for GET single vehicle detail API """
    valid_vehicle_list = [ ]
    invalid_query_set = ['1236']
    def setUp(self):
        self.first = Vehicle.objects.create(vid='1234', vin='1213231', color='Metallic Silver', doorCount=4, driveTrain='v8')
        self.valid_vehicle_list.append(self.first)
        self.second = Vehicle.objects.create(
            vid='1235', vin='1235AZ91XP', color='Forest Green', doorCount=2, driveTrain='electric')
        self.valid_vehicle_list.append(self.second)
        
    def test_get_valid_single_vehicle(self):
        """ Check validity of each single vehicle in the list """
        for vehicle in self.valid_vehicle_list:
            response = client.get(
                reverse('get-vehicle-detail', kwargs={'pk': vehicle.pk}))
            # response = client.get('get-vehicle-detail/1234')
            vehicle_obj = Vehicle.objects.get(pk=vehicle.pk)
            serializer = VehicleSerializer(vehicle_obj)
            self.assertEqual(response.data, serializer.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_vehicle(self):
        """check response error for invalid query parameter """
        for item in self.invalid_query_set:
            response = client.get(
                reverse('get-vehicle-detail', kwargs={'pk': item}))
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        


class CreateNewVehicleTest(TestCase):
    """ Test module for creating a new vehicle by POST"""
    valid_payload_list = [ ]
    invalid_payload_list = []
    HEADER = {"content-type": "application/json"}
    URL = "http://127.0.0.1:8000/vehicles/"
    
    def setUp(self):
        # self.valid_payload_first = {
        #     'vid': '1236',
        #     'vin': '1213232',
        #     'color': 'Metallic Silver',
        #     'doorCount': 4,
        #     'driveTrain': 'v7'
        # }
 
 #       self.valid_payload_list.append(self.valid_payload_first)
        
        # self.valid_payload_second = {
        #     'vid': '1237',
        #     'vin': '1235AZ91XM',
        #     'color': 'Forest Green',
        #     'doorCount': 2,
        #     'driveTrain': 'electric'
        # }
        # self.valid_payload_list.append(self.valid_payload_second)
        
        self.invalid_payload_id = {
            'vid': '',
            'vin': '1213231',
            'color': 'Metallic Silver',
            'doorCount': 4,
            'driveTrain': 'v8'
        }
        self.invalid_payload_list.append(self.invalid_payload_id)
        
        self.invalid_payload_door = {
            'vid': '1234',
            'vin': '1213231',
            'color': 'Metallic Silver',
            'doorCount': 6,
            'driveTrain': 'v8'
        }
        self.invalid_payload_list.append(self.invalid_payload_door)
        
   # def test_create_valid_vehicle(self):
    #save this valid create test to test_api.py
 
            
    def test_create_invalid_vehicle(self):
        for invalid_payload in self.invalid_payload_list:
            response = requests.post(url=self.URL, headers=self.HEADER, data=json.dumps(invalid_payload))
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
 

# class GetDoorsForVehicleTest(TestCase):
#     """ Test module for GET doors security of a single vehicle  """
#     valid_doors_list = [ ]
#     invalid_query_set = [ ]
#     def setUp(self):
#         self.vehicle = Vehicle.objects.create(
#             vid='1235', vin='1235AZ91XP', color='Forest Green', doorCount=2, driveTrain='electric')
#         self.first = self.vehicle.doors.create(
#             location='frontLeft', locked=True, vehicle='1235')
#         self.valid_doors_list.append(self.first)
#         self.second = self.vehicle.doors.create(
#             location='frontRight', locked=True, vehicle='1235')
#         self.valid_doors_list.append(self.second)

#     def test_get_valid_doors(self):
#         """ Check validity of door security about a single vehicle  """
#       #  for item in self.valid_doors_list:
#         response = client.get(reverse('get-vehicle-doors', kwargs={'pk': self.vehicle.pk}))
#         print(response.data)
#       # response = client.get('get-vehicle-detail/1234')
#      # vehicle_obj = Vehicle.objects.get(pk=vehicle.pk)
#      # serializer = VehicleSerializer(vehicle_obj)
#      # print(response.data)
#      # self.assertEqual(response.data, serializer.data)
#      # self.assertEqual(response.status_code, status.HTTP_200_OK)
      
#     def _get_invalid_single_vehicle(self):
#         """check response error for invalid query parameter """
#         for item in self.invalid_query_set:
#             response = client.get(
#                 reverse('get-vehicle-detail', kwargs={'pk': item}))
#             self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
