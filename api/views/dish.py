from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from api.api_utils import recipe_rate
from api.api_utils.recipe_rate import recipe_rate
from api.models.dish import Dish
from api.serializers.dish_crud import CreateDishSerializer, MyRecipeSerializer

User = get_user_model()


class CreateDishGenericAPIView(GenericAPIView):
    permission_classes = IsAuthenticated
    serializer_class = CreateDishSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class MyRecipeGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = MyRecipeSerializer

    def get(self, request):
        my_recipe = Dish.objects.filter(user_id=request.user.id)
        serializer = self.get_serializer(my_recipe, many=True)
        serialized_data = serializer.data
        for recipe in serialized_data:
            recipe['author_name'] = User.objects.get(id=request.user.id).first_name
            recipe['rate'] = recipe_rate(dish_id=recipe['id'])
        return Response(serialized_data, status=200)


