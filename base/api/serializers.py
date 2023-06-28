from base.models import CustomUser,Activity

from rest_framework import serializers



    
    
class ListUserSerializer(serializers.ModelSerializer):
      class Meta:
        model= CustomUser
        fields=("username","batch","role","activity")


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Activity
        fields=("user","name","date")

class UserProfileSerializer(serializers.ModelSerializer):
        activity = ActivitySerializer(many=True)

        class Meta:
           model=CustomUser
           fields=("id","username","email","batch","role","gender","admission_number","dob","phone_no","guardian","guardian_no","teacher_remarks","activity")

class UserProfileUpdateSerializer(serializers.ModelSerializer):
        class Meta:
           model=CustomUser
           fields=("id","username","email","batch","role","gender","admission_number","dob","phone_no","guardian","guardian_no","teacher_remarks")