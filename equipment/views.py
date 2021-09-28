from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from datetime import date
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView


class EquipmentList(ListView):
    model = Equipment
    template_name = 'equipment.html'


class EquipmentView(APIView):
    def get(self, request):
        equipment = Equipment.objects.all()
        serializer = EquipmentSerializer(equipment, many=True)
        return Response({"equipment": serializer.data})

    def post(self, request):
        equipment = request.data.get('equipment')
        serializer = EquipmentSerializer(data=equipment)
        if serializer.is_valid(raise_exception=True):
            equipment_saved = serializer.save()
        return Response({"success": "Equipment '{}' created successfully".format(equipment_saved.name)})


class StaffList(ListView):
    model = Employee
    template_name = 'staff.html'

class MainPage(TemplateView):
    template_name = 'main.html'
