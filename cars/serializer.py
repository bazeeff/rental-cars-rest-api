from rest_framework import serializers
from .models import User, Car
from django.core.validators import EmailValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
import json
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-id']
        model = Car
        fields = ("id", "name", "created_date", "added_date")


class UserSerializer(serializers.ModelSerializer):

    cars = CarSerializer(many=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'cars')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

        depth = 1


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=255,
        min_length=6,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'cars']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def validate(self, attrs):
            email = attrs.get('email', '')
            username = attrs.get('username', '')

            # if not email.isalemail:
            #     raise serializers.ValidationError(
            #         "Username should contain only alphanumeric characters"
            #     )
            #
            # if not username.isalnum():
            #     raise serializers.ValidationError(
            #         "Username should contain only alphanumeric characters"
            #     )
            return attrs

    def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user


