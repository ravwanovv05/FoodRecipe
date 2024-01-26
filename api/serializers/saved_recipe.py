from rest_framework.serializers import ModelSerializer
from api.models.dish import Dish


class SavedRecipeSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'cocking_time')
