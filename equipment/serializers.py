from rest_framework import serializers


class EquipmentSerializer(serializers.Serializer):
    name = serializers.CharField()
    serial = serializers.CharField()
    in_use = serializers.CharField()

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