from django.urls import path

from users.views import SignupView, TokenView

urlpatterns = [
    path('auth/signup/', SignupView.as_view()),
    path('auth/token/', TokenView.as_view()),
]
