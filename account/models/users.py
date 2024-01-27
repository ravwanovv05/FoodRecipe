from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField('Username', max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField('Email', unique=True, null=False, blank=False)
    avatar = models.ImageField('Avatar', upload_to='pic')
    bio = models.CharField('Biography', max_length=255, null=True, blank=True)
    location = models.CharField('Location', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
