from rest_framework import serializers

from .models import *


class PermissionSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    desc = serializers.CharField()

    def create(self, validated_data):
        return Permission.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.desc = validated_data.get('desc', instance.desc)
        instance.save()
        return instance
