from rest_framework import serializers
from .models import Equipment


class EquipmentSerializer(serializers.Serializer):
    name = serializers.CharField()
    serial = serializers.IntegerField()


    def create(self, validated_data):
        return Equipment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.serial = validated_data.get('serial', instance.serial)
        instance.in_use = validated_data.get('in_use', instance.in_use)
        instance.save()
        return instance
