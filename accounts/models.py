from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):

    class Meta:
        # Add the related_name arguments
        # to avoid clashes with the default User model
        # reverse accessors
        permissions = [('view_user', 'Can view user')]
        default_permissions = []
        swappable = 'AUTH_USER_MODEL'
