from django.test import TestCase
from django.shortcuts import get_object_or_404
import json
import requests
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


VEHICLE_LIST = ["1234", "1235"]
VEHICLE_NUM = len(VEHICLE_LIST)

class PostVehicleTest(TestCase):
    """ Test module for POST to vehicle list of Smart API using responses from GM API """
    URL_SMART = "http://127.0.0.1:8000/vehicles/"
    URL_GM = "http://gmapi.azurewebsites.net/getVehicleInfoService/"
    HEADER = {"content-type": "application/json"}
    vd_list = [ ]
        
    def setUp(self):
    # """Retrieving vehicle data through posting to GM API endpoint """
      #delete all the vehicle objects before creating new ones
        for x in range(0, VEHICLE_NUM):
            self.vd_list.append({})
            
        for i in range(0, len(self.vd_list)):
            #Retrieving vehicle data through posting to GM API endpoint
            data = {"id":VEHICLE_LIST[i], "responseType":"JSON"}
            response = requests.post(url=self.URL_GM, headers=self.HEADER, json=data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            resp_str = response.text
            resp_dict = json.loads(resp_str)
            #Construct data payload for sending post request to Smart API endpoint
            value_list = list(resp_dict['data'].values())
            fields = [ ]
            for info in value_list:
                fields.append(info['value'])
            self.assertEqual(len(value_list), 5) #make sure there are 5 attributes of a vehicle from GM
            self.vd_list[i]['vid'] = VEHICLE_LIST[i]
            self.vd_list[i]['vin'] = fields[0]
            self.vd_list[i]['color'] = fields[1]
            if(fields[2]):
                self.vd_list[i]['doorCount'] = 4
            elif(fields[3]):
                self.vd_list[i]['doorCount'] = 2
            self.vd_list[i]['driveTrain'] = fields[4]
            
         
    def test_post_vehicle(self):
        # get Smart API post response, then using get request to retrieve created vehicle
        for i in range(0, len(self.vd_list)):
            #before posting, check if the object exists or not
            url = self.URL_SMART + VEHICLE_LIST[i]
            check = requests.get(url)
            if(check.status_code == status.HTTP_200_OK):
                delete = requests.delete(url)
                self.assertEqual(delete.status_code, status.HTTP_204_NO_CONTENT)
            check_again = requests.get(url)
            self.assertEqual(check_again.status_code, status.HTTP_404_NOT_FOUND)
            payload = self.vd_list[i]
            response = requests.post(url=self.URL_SMART, json=payload)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)




class postDoorsTest(TestCase):
    """ Test module for POST to  Smart API vehicle/doors endpoint using info from GM """

    URL_GM = "http://gmapi.azurewebsites.net/getSecurityStatusService"
    HEADER = {"content-type": "application/json"}
    BASE_URL = "http://127.0.0.1:8000/vehicles/"
    SUFFIX = "/doors/"
    sd_list = [ ]

    def strToBool(self, s):
        t = True
        f = False
        if(s == "True"):
            return t
        elif(s == "False"):
            return f

    def setUp(self):
        #retrieving vehicle security data through posting to GM API endpoint
        #delete all the security objects before creating new ones
        for x in range(0, VEHICLE_NUM):
            self.sd_list.append([])

        for i in range(0, len(self.sd_list)):
            #Retrieving vehicle data through posting to GM API endpoint
           
            data = {"id":VEHICLE_LIST[i], "responseType":"JSON"}
            response = requests.post(url=self.URL_GM, headers=self.HEADER, json=data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            resp_str = response.text
            resp_dict = json.loads(resp_str)
            #Construct data payload for sending post request to Smart API endpoint
            sec_data = resp_dict['data']['doors']['values']
            for sec in sec_data:
                temp = {}
                temp['location'] = sec['location']['value']
                temp['locked'] = self.strToBool(sec['locked']['value'])
                temp['vehicle'] = VEHICLE_LIST[i]
                self.sd_list[i].append(temp)
        

    def test_post_security(self):
        # get Smart API post response, then using get request to retrieve created security for vehicle
 
        for i in range(0, len(self.sd_list)):
            for sd in self.sd_list[i]:
                url = self.BASE_URL + VEHICLE_LIST[i] + self.SUFFIX
                data = sd
                response = requests.post(url=url, json=data)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
         
 
class postEnergyTest(TestCase):
    """Test module for POST energy info from GM to Smart vehicle/<energyType> endpoint"""
    
    URL_GM = "http://gmapi.azurewebsites.net/getEnergyService"
    HEADER = {"content-type": "application/json"}
    BASE_URL = "http://127.0.0.1:8000/vehicles/"
    SUFFIX_F = "/fuel/"
    SUFFIX_B = "/battery/"
    ed_list = []

    def strToFloat(self, s):
        if(s == 'null' or s == 'Null'):
            return None
        return float(s)
    
    def setUp(self):
        for i in range(0, VEHICLE_NUM):
            data = {"id":VEHICLE_LIST[i], "responseType":"JSON"}
            response = requests.post(url=self.URL_GM, headers=self.HEADER, json=data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            e_dict = json.loads(response.text)
            e_list = list(e_dict['data'].values())
            fuel_dict = {}
            bat_dict = {}
            fuel_dict['percent']  = self.strToFloat(e_list[0]['value'])
            fuel_dict['vehicle'] = VEHICLE_LIST[i]
            bat_dict['percent']  = self.strToFloat(e_list[1]['value'])
            bat_dict['vehicle'] = VEHICLE_LIST[i]
            t_list = []
            t_list.append(fuel_dict)
            t_list.append(bat_dict)
            self.ed_list.append(t_list)
       
    def test_post_energy(self):
      
        for i in range(0, len(self.ed_list)):
            l = self.ed_list[i]
            url_tank = self.BASE_URL + VEHICLE_LIST[i] + self.SUFFIX_F
            data_tank = l[0]
            response_tank = requests.post(url=url_tank, json=data_tank)
            self.assertEqual(response_tank.status_code, status.HTTP_201_CREATED)
            url_bat = self.BASE_URL + VEHICLE_LIST[i] + self.SUFFIX_B
            data_bat = l[1]
            response_bat = requests.post(url=url_bat, json=data_bat)
            self.assertEqual(response_bat.status_code, status.HTTP_201_CREATED)
            
           
class postEngineTest(TestCase):
    """Test module for posting engine check request to Smart API vehicle/engine endpoint and get status from GM"""

    URL_GM = "http://gmapi.azurewebsites.net/actionEngineService"
    HEADER = {"content-type": "application/json"}
    BASE_URL = "http://127.0.0.1:8000/vehicles/"
    SUFFIX = "/engine/"
    COMMAND_LIST = {"START_VEHICLE", "STOP_VEHICLE"}
    ACTION_LIST = {"START", "STOP"}
    ed_list = []

    def setUp(self):
        for i in range(0, VEHICLE_NUM):
            engine = []
            for command in self.COMMAND_LIST:
                data = {"id":VEHICLE_LIST[i], "command":command, "responseType":"JSON"}
                response = requests.post(url=self.URL_GM, headers=self.HEADER, json=data)
                self.assertEqual(response.status_code, status.HTTP_200_OK)
                s = (json.loads(response.text))['actionResult']['status']
                eng = {}
                if(command == "START_VEHICLE"):
                    eng['action'] = "START"
                elif(command == "STOP_VEHICLE"):
                    eng['action'] = "STOP"
                if(s == "EXECUTED"):
                    eng['status'] = "success"
                elif(s == "FAILED"):
                    eng['status'] = "error"
                eng['vehicle'] = VEHICLE_LIST[i]
                engine.append(eng)
            self.ed_list.append(engine)

    def test_post_engine(self):
        for i in range(0, VEHICLE_NUM):
            url = self.BASE_URL + VEHICLE_LIST[i] + self.SUFFIX
            for action in self.ACTION_LIST:
                data = {}
                data['vehicle'] = VEHICLE_LIST[i]
                data['action'] = action
                if(action == "START"):
                    data['status'] = self.ed_list[i][0]['status']
                elif(action == "STOP"):
                    data['status'] = self.ed_list[i][1]['status']
                response = requests.post(url=url, json=data)
                self.assertEqual(response.status_code, status.HTTP_201_CREATED)
