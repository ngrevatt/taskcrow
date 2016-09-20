from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile


class CustomerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Customer


class ServiceProviderSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = ServiceProvider


class VerificationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Verification


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task

