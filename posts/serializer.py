from rest_framework.serializers import ModelSerializer
from accounts.serializer import UserRegistrationSerializer
from posts.models import Post


class PostSerializer(ModelSerializer):
    author =  UserRegistrationSerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'

