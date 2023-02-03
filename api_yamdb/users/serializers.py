from rest_framework import serializers

from users.models import User


class SendConfirmationCodeSerializer(serializers.ModelSerializer):
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


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
        model = User
