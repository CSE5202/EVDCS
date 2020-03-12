from django.contrib.auth.models import User, Group
from rest_framework import serializers

from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)
User = get_user_model()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']