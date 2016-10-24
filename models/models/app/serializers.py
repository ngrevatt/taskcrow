from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User


class ServiceProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceProvider


class VerificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Verification


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        depth = 2

