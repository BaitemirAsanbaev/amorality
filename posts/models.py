from django.db import models
from accounts.models import User
from django.conf import settings


class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
