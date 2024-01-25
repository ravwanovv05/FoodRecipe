from django.db import models

from api.models.dish import Dish


class Media(models.Model):
    image = models.ImageField('Image', upload_to='pic')
    file = models.FileField('File', upload_to='video')

    dish_id = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'

    def __str__(self):
        return f"{self.dish_id}"
