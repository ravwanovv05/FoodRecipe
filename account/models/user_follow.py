from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class UserFollow(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('from_user', 'to_user')
        verbose_name = 'User Follow'
        verbose_name_plural = 'Users Follow'

    def __str__(self):
        return f'{self.from_user} - {self.to_user}'
