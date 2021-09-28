from rest_framework import serializers
from .models import Equipment


class EquipmentSerializer(serializers.Serializer):
    name = serializers.CharField()
    serial = serializers.IntegerField()
    # in_use = serializers.CharField()

    def create(self, validated_data):
        return Equipment.objects.create(**validated_data)

# так делал Дима
# class EquipmentSerializer(ModelSerializer):
#     class Meta:
#         model = Equipment
#         fields = ('id',
#                   'photo',
#                   'item_number',
#                   'name',
#                   'in_use_by',
#                   'paid_by',
#                   'price',
#                   'comment',
#                   'employee_start_date',
#                   'configuration'
#                   )