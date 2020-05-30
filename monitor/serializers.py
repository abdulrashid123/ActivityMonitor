from rest_framework import serializers
from .models import User, Activity

# Serializers for Activity Model


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('start_time','end_time')

# Use child serializer in Parent serializer to get all object in User serializers


class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivitySerializer(many=True)

    class Meta:
        model = User
        fields = ['id','real_name','tz','activity_periods']



