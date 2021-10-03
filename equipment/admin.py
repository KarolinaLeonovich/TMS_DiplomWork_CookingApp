from django.contrib import admin
from .models import *

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'position')

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial', 'in_use')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(PositionQuantity)
class PositionQuantityAdmin(admin.ModelAdmin):
    list_display = ('position_name', 'position_quantity')

