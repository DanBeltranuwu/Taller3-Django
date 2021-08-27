import measurements
from django.shortcuts import render
from .logic.logic_measurements import get_all_measurements, get_measurement_by_pk, delete_measurement_by_pk, update_measurement_by_pk
from django.http import HttpResponse
from django.core import serializers

def get_measurements(request):
    measurements = get_all_measurements()
    measurement_list = serializers.serialize('json', measurements)
    return HttpResponse(measurement_list,content_type= 'application/json')

def get_measurement(request, param):
    measurement = get_measurement_by_pk(param)
    measurement_chosen = serializers.serialize('json', measurement)
    return HttpResponse(measurement_chosen,content_type= 'application/json')

def delete_measurement(request, param):
    delete_measurement_by_pk(param)
    return HttpResponse("Measurement "+ str(param) + " was deleted.")

def update_measurement(request, param, value, unit, place):
    update_measurement_by_pk(param, value, unit, place)
    return HttpResponse("Measurement "+ str(param) + " was updated.")