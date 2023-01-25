from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from reviews.models import Review, Comments


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Оценки."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('title', 'author', 'text', 'pub_date', 'rating')

    def validate(self, data):
        if self.context['request'].method != 'POST':
            return data

        title_id = self.context['view'].kwargs.get('title_id')
        author = self.context['request'].user
        if Review.objects.filter(author=author, title=title_id).exists():
            raise serializers.ValidationError(
                'Можно написать лишь один отзыв.'
            )
        return data

    def validate_score(self, value):
        if not 1 <= value <= 10:
            raise serializers.ValidationError(
                'Оценкой должно быть число от 1 до 10.'
            )
        return value


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментария."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'text', 'author', 'pub_date')
