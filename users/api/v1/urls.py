from django.urls import path
from users.api.v1.views import (
    UserRegisterCreateAPIView,
    UserLoginAPIView, 
    TokenRefreshAPIView
    )

urlpatterns = [
    path('register/', UserRegisterCreateAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshAPIView.as_view(), name='token_refresh'),
]
