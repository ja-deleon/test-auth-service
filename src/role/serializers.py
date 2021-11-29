from rest_framework import serializers

from .models import *

class RoleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    desc = serializers.CharField()
    permissions = serializers.CharField()

    def create(self, validated_data):
        return Role.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.permissions = validated_data.get('permissions', instance.permissions)
        instance.save()
        return instance
