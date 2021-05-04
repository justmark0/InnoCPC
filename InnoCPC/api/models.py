from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_id = models.BigIntegerField()  # user_id from Telegram
    username = models.CharField(max_length=50, unique=True)
    cf_login = models.CharField(max_length=50, unique=True)
    timus_login = models.CharField(max_length=50, unique=True)
    cf_points = models.IntegerField()
    timus_points = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['username']),
        ]


class Team(models.Model):
    name = models.CharField(max_length=150)


class TeamMember(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    team = models.OneToOneField(Team, on_delete=models.CASCADE)

