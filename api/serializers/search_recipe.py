from rest_framework.serializers import ModelSerializer

from api.models.dish import Dish


class SearchRecipeSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'user_id', 'rate')