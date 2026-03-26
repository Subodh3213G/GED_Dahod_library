from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from .api_views import (
    CustomTokenObtainPairView, api_sitemap, RegisterView, LogoutView, ChangePasswordView, DeleteUserView
)

urlpatterns = [
    # JWT Authentication Endpoints
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    # Generic API Sitemap
    path('sitemap/', api_sitemap, name='api_sitemap'),
    
    # User Auth Endpoints
    path('login/', CustomTokenObtainPairView.as_view(), name='api_login'), # Alias for token/
    path('register/', RegisterView.as_view(), name='api_register'),
    path('logout/', LogoutView.as_view(), name='api_logout'),
    path('update-password/', ChangePasswordView.as_view(), name='api_update_password'),
    path('delete/', DeleteUserView.as_view(), name='api_delete_user'),
]
