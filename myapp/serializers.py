from django.contrib.auth.models import User
from rest_framework import serializers

from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
from accounts.models import Phonenumber
from .models import *



class PhonenumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonenumber
        fields = '__all__'

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'
User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [ 'username', 'email']


class driverSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = driver
        fields = '__all__'
class assignementSerializer(serializers.ModelSerializer):
    class Meta:
        model = assign_vehicle
        fields = '__all__'

class deploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = deployment
        fields = '__all__'
class MachineDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = machine_data
        fields = '__all__'
class attendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
class penaltySerializer(serializers.ModelSerializer):

    class Meta:
        model = penalty
        fields = '__all__'
class stationSerializer(serializers.ModelSerializer):

    class Meta:
        model = station
        fields = '__all__'