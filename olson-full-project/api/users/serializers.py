from select import select
from rest_framework import serializers
from users.models import User

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # def to_representation(self, instance):
    #     print(instance)
    #     return {
    #         'username': instance['username'],
    #         'email': instance['email'],
    #         'is_active': instance['is_active'],
    #         'is_verified': instance['is_verified'],
    #     }

#Custom Serializer for creating data for the first time.

class UserCreateSerializer(serializers.ModelSerializer):
    
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
        data = super().to_representation(instance)
        return {
            'username': data['username'],
            'email': data['email'],
            'is_active': data['is_active'],
            'is_verified': data['is_verified'],
        }

# Using a Serializer for updating data

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
        
    # def to_representation(self, instance): 
    #     data = super().to_representation(instance)
    #     return data

# Using a Model Serializer for updating data

# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


#     def update(self, instance, validated_data):
#         data = super().update(instance, validated_data)
#         data.save()
#         return data

class UserChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(max_length=100, required=True, write_only=True)
    password = serializers.CharField(max_length=100, required=True, write_only=True)
    password2 = serializers.CharField(max_length=100, required=True, write_only=True)

    def validate_old_password(self, value):
        user = self.instance

        if not user.check_password(value):
            raise serializers.ValidationError({
                "msg":"Wrong current password."
            })
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({
                "msg":"Passwords didn't match.  Try again."
            })
        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance