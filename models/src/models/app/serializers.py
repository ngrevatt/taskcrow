from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedIdentityField(
            view_name="userprofile-detail")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "profile")


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = UserProfile


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = Customer


class ServiceProviderSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = ServiceProvider


class VerificationSerializer(serializers.HyperlinkedModelSerializer):
    service_provider = serializers.HyperlinkedIdentityField(
            view_name="serviceprovider-detail")

    class Meta:
        model = Verification


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedIdentityField(view_name="user-detail")

    class Meta:
        model = Task

