from django.urls import include, path
<<<<<<< HEAD
from rest_framework.routers import DefaultRouter

from api.views import (
    CategoryViewSet,
    CommentViewSet,
    GenreViewSet,
    ReviewViewSet,
    TitleViewSet,
)

app_name = 'api'

router = DefaultRouter()
router.register(
    r'categories', CategoryViewSet, basename='categories'
)
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)
=======
from rest_framework.routers import SimpleRouter

from .views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                    ReviewViewSet, TitleViewSet, UserViewSet)

app_name = 'api'

router = SimpleRouter()

router.register('categories', CategoryViewSet, basename='сategories')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
router.register('genres', GenreViewSet, basename='genres')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet,
                basename='reviews')
router.register('titles', TitleViewSet, basename='titles')
router.register('users', UserViewSet, basename='users')

>>>>>>> 3543b90acf979d28dd806b8beaee95eefd99211d

urlpatterns = [
    path('v1/', include(router.urls)),
]
