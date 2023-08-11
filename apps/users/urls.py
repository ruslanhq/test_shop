from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserRegistrationView

urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='user-register'),
    path('api/login/', TokenObtainPairView.as_view(), name='user-login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
