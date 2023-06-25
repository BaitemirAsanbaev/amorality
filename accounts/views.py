from rest_framework import generics, views
from .serializer import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import models


class RevokedToken(models.Model):
    jti = models.CharField(max_length=255)
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get the refresh token from the request data
            refresh_token = request.data["refresh_token"]

            # Decode the refresh token to obtain the jti value
            token = RefreshToken(refresh_token)
            jti = token["jti"]

            # Add the jti value to the revoked tokens model
            RevokedToken.objects.create(jti=jti)

            return Response({"detail": "Logout successful."})

        except Exception as e:
            return Response({"detail": str(e)}, status=400)