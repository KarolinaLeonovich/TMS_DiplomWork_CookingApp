from django.urls import path

from .views import *

urlpatterns = [
    path('equipment/', EquipmentList.as_view(), name='equipment'),
    path('equipment_api/', EquipmentView.as_view()),
]