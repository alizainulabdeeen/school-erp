from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.api.v1.serializers import UserRegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class UserRegisterCreateAPIView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

class UserLoginAPIView(TokenObtainPairView):
    permission_classes = [AllowAny]

class TokenRefreshAPIView(TokenRefreshView):
    pass
