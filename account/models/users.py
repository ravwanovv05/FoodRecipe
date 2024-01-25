from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    full_name = models.CharField('Full Name', max_length=255, null=True, blank=True)
    email = models.EmailField('Email', unique=True)
    username = models.CharField('Username', max_length=255, null=True, blank=True)
    password = models.CharField('Password', max_length=50)
    avatar = models.ImageField('Avatar', upload_to='pic')
    bio = models.CharField('Biography', max_length=255, null=True, blank=True)
    location = models.CharField('Location', max_length=255, null=True, blank=True)
    following = models.PositiveBigIntegerField('Following', default=0)
    followers = models.PositiveBigIntegerField('Followers', default=0)
    joined_at = models.DateTimeField('Joined At', auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.full_name


