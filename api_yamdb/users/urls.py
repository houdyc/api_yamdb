from django.urls import include, path
from rest_framework import routers

from users.views import SignupView, TokenView, UsersViewSet

router = routers.DefaultRouter()
router.register('users', UsersViewSet)

urlpatterns = [
    path('auth/signup/', SignupView.as_view()),
    path('auth/token/', TokenView.as_view()),
    path('', include(router.urls)),
]
