from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name="measurementList"),
    path('get/<int:param>', views.get_measurement, name="measurementGet"),
    path('delete/<int:param>', views.delete_measurement, name="measurementDelete"),
    path('update/<int:param>/<int:value>-<str:unit>-<str:place>', views.update_measurement, name="measurementUpdate")
]