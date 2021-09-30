from django.views.generic import TemplateView
from rest_framework.generics import get_object_or_404

from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import ListView, FormView



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

    def put(self, request, pk):
        saved_equipment = get_object_or_404(Equipment.objects.all(), pk=pk)
        data = request.data.get('equipment')
        serializer = EquipmentSerializer(instance=saved_equipment, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            equipment_saved = serializer.save()
        return Response({
            "success": "Equipment '{}' updated successfully".format(equipment_saved.title)
        })

    def delete(self, request, pk):
        equipment = get_object_or_404(Equipment.objects.all(), pk=pk)
        equipment.delete()
        return Response({
            "message": "Equipment with id `{}` has been deleted.".format(pk)
        }, status=204)


class StaffList(ListView):
    model = Employee
    template_name = 'staff.html'


class MainPage(TemplateView):
    template_name = 'main.html'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = 'http://127.0.0.1:8000/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('http://127.0.0.1:8000/')

