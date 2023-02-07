from django.shortcuts import get_object_or_404
<<<<<<< HEAD
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins, status, filters
=======
from rest_framework import viewsets, status
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin)
from rest_framework.viewsets import GenericViewSet
<<<<<<< HEAD
from rest_framework.pagination import PageNumberPagination

from .filters import FilterTitle
=======

>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
from .serializers import (CommentSerializer, ReviewSerializer,
                          CategorySerializer, GenreSerializer,
                          TitleReadSerializer, TitleWriteSerializer,
                          AdminUserSerializer, NotAdminUserSerializer)
<<<<<<< HEAD
from users.permissions import (
    IsAdminOrReadOnlyPermission,
    IsAdminPermission,
    IsAuthorPermission,
    IsModeratorPermission,
)
from reviews.models import Review, Title, User, Category, Genre


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = [IsAdminOrReadOnlyPermission]
    filter_backends = (DjangoFilterBackend,)
    filter_class = FilterTitle
    ordering_fields = ('name',)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return TitleReadSerializer
        return TitleWriteSerializer
=======
from .permissions import (IsAuthorPermission, IsAdminPermission,
                          IsModeratorPermission, IsAdminOrReadOnlyPermission)
from reviews.models import Review, Title, User, Category, Genre

from .permissions import IsAdminPermission, IsAuthorPermission
from .permissions import IsModeratorPermission
from .serializers import CommentSerializer, ReviewSerializer
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d


class ReviewViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки отзывов."""

    serializer_class = ReviewSerializer
    permission_classes = [
        IsAuthorPermission,
        IsAdminPermission,
        IsModeratorPermission,
    ]
<<<<<<< HEAD

    def get_title(self):
        return get_object_or_404(
            Title,
            id=self.kwargs.get('title_id')
        )
=======
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Review, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    """Вьюсет для обработки комментариев."""

    serializer_class = CommentSerializer
    permission_classes = [
        IsAuthorPermission,
        IsAdminPermission,
        IsModeratorPermission,
    ]
<<<<<<< HEAD
    pagination_class = PageNumberPagination

    def get_review(self):
        return get_object_or_404(
            Review,
            id=self.kwargs.get('review_id'),
        )
=======
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review_id=review.id)


<<<<<<< HEAD
class CategoryViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin, viewsets.GenericViewSet):
=======
class CategoryViewSet(ListModelMixin, CreateModelMixin,
                      DestroyModelMixin, GenericViewSet):
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnlyPermission]

<<<<<<< HEAD
    @action(
        detail=False, methods=['delete'],
        url_path=r'(?P<slug>\w+)',
        lookup_field='slug', url_name='category_slug'
    )
    def get_category(self, request, slug):
        category = self.get_object()
        serializer = CategorySerializer(category)
        category.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class GenreViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnlyPermission]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    @action(
        detail=False, methods=['delete'],
        url_path=r'(?P<slug>\w+)',
        lookup_field='slug', url_name='category_slug'
    )
    def get_genre(self, request, slug):
        category = self.get_object()
        serializer = CategorySerializer(category)
        category.delete()
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
=======

class GenreViewSet(ListModelMixin, CreateModelMixin,
                   DestroyModelMixin, GenericViewSet):
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
>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d
