from rest_framework.serializers import ModelSerializer

from api.models.dish import Dish


class CreateDishSerializer(ModelSerializer):
    class Meta:
        model = Dish
        fields = '__all__'
        read_only_fields = ('user_id',)

    def create(self, validated_data):
        user_id = self.context['request'].user.id
        return Dish.objects.create(user_id=user_id, **validated_data)

