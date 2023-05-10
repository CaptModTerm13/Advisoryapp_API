from base.models import CustomUser

from rest_framework import serializers



    
    
class ListUserSerializer(serializers.ModelSerializer):
     class Meta:
        model= CustomUser
        fields=("username","batch","role")





class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=("username","batch","role","gender","admission_number")
        