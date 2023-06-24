from rest_framework.permissions import IsAuthenticated
from .serializer import PostSerializer
from rest_framework import generics
from .models import Post

class PostCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def post(self, request):
    #     if serializer.is_valid():
    #         serializer.save(user=request.user)
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
