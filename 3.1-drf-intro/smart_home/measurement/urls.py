from django.contrib import admin
from django.urls import path

from .views import SensorsView, SensorCreateView, SensorUpdateView, MeasurementCreateView, SensorDetailView, SensorDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Sensor/', SensorsView.as_view()),
    path('Sensorcreate/', SensorCreateView.as_view()),
    path('Sensordetail/<pk>/', SensorDetailView.as_view()),
    path('Sensorupdate/<pk>/', SensorUpdateView.as_view()),
    path('Sensordestroy/<pk>/', SensorDestroyView.as_view()),
    path('Measurementcreate/', MeasurementCreateView.as_view()),
]
