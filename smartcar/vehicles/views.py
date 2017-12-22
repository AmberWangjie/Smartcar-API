from django.shortcuts import render
#from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
#our responses are no longer hardwired to a single content type
def vehicle_list(request, format=None):
    """
    List all vehicles, or create a new one.
    """
    if request.method == 'GET':
        vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(vehicles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def vehicle_detail(request, pk, format=None):
    """
    Retrieve, update or delete a vehicle.
    """
    try:
        vehicle = Vehicle.objects.get(pk=pk)
    except Vehicle.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VehicleSerializer(vehicle)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VehicleSerializer(vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def vehicle_security(request, vehicle_pk, format=None):
    """
    Retrieve, create, update or delete a vehicle security.
    """
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_pk)
        doors = vehicle.doors.all()
    except Security.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SecuritySerializer(doors, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = SecuritySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        serializer = SecuritySerializer(security, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        for door in doors:
            door.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def vehicle_fuel(request, vehicle_pk, format=None):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_pk)
        fuel = vehicle.fuelLevel.all()
    except Fuel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FuelSerializer(fuel, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = FuelSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = FuelSerializer(fuel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        fuel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def vehicle_battery(request, vehicle_pk, format=None):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_pk)
        battery = vehicle.batteryLevel.all()
    except Battery.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BatterySerializer(battery, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BatterySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        serializer = BatterySerializer(battery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        battery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view([ 'POST'])
def vehicle_engine(request, vehicle_pk,  format=None):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_pk)
        engine = vehicle.engineStatus.all()
    except Engine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'POST':
        request_serializer = requestEngineSerializer(data=request.data)
        if(request_serializer.is_valid()):
            request_serializer.save()
        response_serializer = responseEngineSerializer(data=request.data)
        if(response_serializer.is_valid()):
            response_serializer.save()
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(request_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
