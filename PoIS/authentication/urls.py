from django.urls import path
from .views import CreateUserView, ObtainTokenView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', ObtainTokenView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
