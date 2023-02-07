from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import EmailValidator
from rest_framework import serializers

from users.models import User


def MeValidator(value):
    if value.lower() == 'me':
        raise serializers.ValidationError(
            "Использовать имя 'me' в качестве `username` запрещено."
        )
    return value


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(
        min_length=1,
        max_length=150,
        required=True,
        allow_blank=False,
        validators=[MeValidator, ASCIIUsernameValidator()],
    )
    email = serializers.EmailField(
        min_length=5,
        max_length=254,
        required=True,
        allow_blank=False,
    )


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
        return MeValidator(value)


class UserSerializer(AdminUserSerializer):
    """Сериализатор для пользователя - не администратора."""

    role = serializers.CharField(read_only=True)
