from django.db import models
from account.models.users import User
from api.models.dish import Dish


class SavedDish(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Saved Dish"
        verbose_name_plural = "Saved Dishes"

    def __str__(self):
        return f"{self.user_id} - {self.dish_id}"
