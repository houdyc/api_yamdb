from django.core.exceptions import ValidationError
from rest_framework import serializers

from users.models import User


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'email',
            'username',
        )
        model = User

    def validate_username(self, value):
        if value.lower() == 'me':
            raise ValidationError(
                "Использовать имя 'me' в качестве `username` запрещено."
            )
        return value


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
        model = User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'bio',
            'email',
            'first_name',
            'last_name',
            'role',
            'username',
        )
        model = User

    def validate_username(self, value):
        if value.lower() == 'me':
            raise ValidationError(
                "Использовать имя 'me' в качестве `username` запрещено."
            )
        return value


class MeSerializer(serializers.ModelSerializer):
    role = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            'bio',
            'email',
            'first_name',
            'last_name',
            'role',
            'username',
        )
