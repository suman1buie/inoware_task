from rest_framework import serializers
from . models import UserProfile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','profile_pic']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']