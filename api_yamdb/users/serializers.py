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
