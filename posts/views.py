from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import Post
from .serializer import PostSerializer
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

class PostCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def perform_create(self, serializer):
        # Extract the JWT token from the request headers
        auth_header = self.request.headers.get('Authorization')
        token = auth_header.split(' ')[1] if auth_header else None

        if token:
            # Decode the JWT token using rest_framework_simplejwt
            decoded_token = AccessToken(token)

            # Retrieve the user object based on the decoded token
            user = decoded_token.payload.get('user_id')
            user_obj = User.objects.get(id=user)

            # Assign the user as the author of the new post
            serializer.save(author=user_obj)
        else:
            # Handle the case where the token is not provided or invalid
            # Depending on your requirements, you may want to raise an error or handle it differently
            # This is just a basic example
            serializer.save()  # Save the post without assigning an author
