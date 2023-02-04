from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet

from .serializers import (CommentSerializer, ReviewSerializer, CategorySerializer,
                          GenreSerializer, TitleReadSerializer, TitleWriteSerializer,
                          AdminUserSerializer, NotAdminUserSerializer)
from .permissions import (IsAuthorPermission, IsAdminPermission,
                          IsModeratorPermission, IsAdminOrReadOnlyPermission)
from reviews.models import Review, Title, User, Category, Genre

from .permissions import IsAdminPermission, IsAuthorPermission
from .permissions import IsModeratorPermission
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки отзывов."""

    serializer_class = ReviewSerializer
    permission_classes = [
        IsAuthorPermission,
        IsAdminPermission,
        IsModeratorPermission,
    ]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('review_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review_id=review.id)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки комментариев."""

    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorPermission,
        IsAdminPermission,
        IsModeratorPermission,
    ]

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('title_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review_id=review.id)


class CategoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnlyPermission]


class GenreViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnlyPermission]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAdminOrReadOnlyPermission]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TitleReadSerializer
        return TitleWriteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAuthenticated, IsAdminPermission]

    @action(methods=['get', 'patch'], detail=False,
            permission_classes=(IsAuthenticated), url_path='me')
    def get_current_user_info(self, request):
        serializer = AdminUserSerializer(request.user)
        if request.method == 'patch':
            if request.user.is_admin:
                serializer = AdminUserSerializer(request.user,
                                                 data=request.data,
                                                 partial=True)
            else:
                serializer = NotAdminUserSerializer(request.user,
                                                    data=request.data,
                                                    partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data)
