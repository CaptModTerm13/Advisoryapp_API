from base.models import CustomUser

from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields=("username","batch","role")