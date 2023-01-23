from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Review, Comments


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Оценки."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('title', 'author', 'text', 'pub_date', 'rating')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментария."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author', 'pub_date')
