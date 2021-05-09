from django.contrib.auth.models import AbstractUser, BaseUserManager
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
import jwt


class UserManager(BaseUserManager):
    """
    Django requires to create User manager if project uses custom users.
    https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#writing-a-manager-for-a-custom-user-model
    """

    def create_user(self, username, user_id):
        if username is None:
            username = f'None_{user_id}'
        user = User(username=username, user_id=user_id)
        user.save()

        return user

    def create_superuser(self, username, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractUser):
    user_id = models.BigIntegerField(db_index=True)  # user_id from Telegram
    username = models.CharField(db_index=True, max_length=50, unique=True)  # null=True
    cf_username = models.CharField(db_index=True, max_length=50, null=True)     # We store usernames to count points
    timus_username = models.CharField(db_index=True, max_length=50, null=True)  # On each platform
    cf_points = models.IntegerField(default=0)
    timus_points = models.IntegerField(default=0)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        dt = datetime.now() + timedelta(days=settings.TOKEN_EXPIRES)

        token = jwt.encode({
            'username': self.username,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token


class Team(models.Model):
    name = models.CharField(max_length=150)


class TeamMember(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    team = models.OneToOneField(Team, on_delete=models.CASCADE)
