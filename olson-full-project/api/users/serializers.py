from unittest.util import _MAX_LENGTH
from wsgiref import validate
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def validate_username(self, value):
        if len(value) < 5:
            raise serializers.ValidationError('Username is too short.')
        return value

    def validate_password(self, value):
        if len(value) < 6 or len(value) > 20:
            raise serializers.ValidationError('Password is too short or too long. Minimum 6 characters and no more than 20 characters.')
        return value

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        return {
            'username':instance.username,
            'email':instance.email
        }


class UserUpdateSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)


    def update(self, instance, validated_data):

        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
        