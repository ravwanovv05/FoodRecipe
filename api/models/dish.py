from django.db import models

from account.models.users import User
from api.models.category import Category


class Dish(models.Model):
    name = models.CharField('Name', max_length=255)
    ingredient = models.TextField('Ingredient', null=True, blank=True)
    procedure = models.TextField('Procedure', null=True, blank=True)
    cocking_time = models.PositiveIntegerField('Cocking', default=0, null=True, blank=True)
    rate = models.PositiveIntegerField('Rate', default=1)
    review = models.TextField('Review', default=1)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField('Created at', auto_now_add=True)

    class Meta:
        verbose_name = 'Dish'
        verbose_name_plural = 'Dishes'

    def __str__(self):
        return self.name
