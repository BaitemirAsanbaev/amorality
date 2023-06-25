from django.urls import path
from .views import PostCreateAPIView, PostGetAPIView, PostUpdateAPIView, PostDeleteAPIView

urlpatterns = [
    path('create/', PostCreateAPIView.as_view(), name='create-post'),
    path('get/', PostGetAPIView.as_view(), name='get-post'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='update-post'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete-post')

]
