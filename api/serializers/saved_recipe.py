from rest_framework.serializers import ModelSerializer, Serializer, IntegerField
from api.models.dish import Dish
from api.models.saved_dish import SavedDish


class SavedRecipeSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'cocking_time', 'image')


class SavedRecipeDetailSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'cocking_time', 'image', 'ingredient', 'video', 'procedure')
