from django.urls import path
from .views import UserRegistrationView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('login/', TokenObtainPairView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
]
