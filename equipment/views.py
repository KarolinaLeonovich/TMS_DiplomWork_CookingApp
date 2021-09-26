from django.shortcuts import render
from django.views.generic import ListView
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


