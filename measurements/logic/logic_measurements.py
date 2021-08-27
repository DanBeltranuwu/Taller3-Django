import measurements
from ..models import Measurement

def get_all_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement_by_pk(param):
    measurement = Measurement.objects.filter(pk = param)
    return measurement

def delete_measurement_by_pk(param):
    Measurement.objects.filter(pk=param).delete()
    
def update_measurement_by_pk(param, pvalue, punit, pplace):
    Measurement.objects.filter(pk=param).update(value = pvalue, unit = punit, place = pplace)