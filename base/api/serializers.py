from base.models import CustomUser

from rest_framework import serializers



    
    
class ListUserSerializer(serializers.ModelSerializer):
     class Meta:
        model= CustomUser
        fields=("username","batch","role")





class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=("username","email","batch","role","gender","admission_number","dob","phone_no","guardian","guardian_no","teacher_remarks")
        