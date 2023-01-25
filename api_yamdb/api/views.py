from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .serializers import CommentSerializer, ReviewSerializer
from .permissions import IsAuthorPermission, IsAdminPermission,\
    IsModeratorPermission
from reviews.models import Review, Title


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки отзывов."""
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthorPermission, IsAdminPermission,
                          IsModeratorPermission]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('review_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review_id=review.id)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки комментариев."""
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorPermission, IsAdminPermission,
                          IsModeratorPermission]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('title_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review_id=review.id)
