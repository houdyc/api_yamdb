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


class AdminUserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователя с ролью администратор."""

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'bio',
            'role',
        )

    def validate_username(self, value):
        if value.lower() == 'me':
            raise ValidationError(
                "Использовать имя 'me' в качестве `username` запрещено."
            )
        return value


class UserSerializer(AdminUserSerializer):
    """Сериализатор для пользователя - не администратора."""

    role = serializers.CharField(read_only=True)
