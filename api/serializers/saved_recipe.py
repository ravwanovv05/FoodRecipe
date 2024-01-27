from rest_framework.serializers import ModelSerializer
from api.models.dish import Dish


class SavedRecipeSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'cocking_time', 'image')


class SavedRecipeDetailSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'cocking_time', 'user_id', 'image', 'ingredient', 'video', 'procedure')
