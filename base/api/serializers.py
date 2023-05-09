from base.models import CustomUser

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6, write_only=True, required=True)

    class Meta:
        model= CustomUser
        fields=("username","batch","role")

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)
    
    
    
class ListUserSerializer(serializers.ModelSerializer):
     class Meta:
        model= CustomUser
        fields=("username","batch","role")
