from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.models.dish import Dish
from api.models.saved_dish import SavedDish
from api.serializers.saved_recipe import SavedRecipeSerializer, SavedRecipeDetailSerializer
from django.contrib.auth import get_user_model
from api.utils.recipe_rate import recipe_rate

User = get_user_model()


class SavedRecipeGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SavedRecipeSerializer

    def get(self, request):
        saved_recipe = SavedDish.objects.filter(user_id=request.user.id)
        saved_recipe_list = []
        for sr in saved_recipe:
            dish = Dish.objects.get(id=sr.dish_id.id)
            serializer = self.get_serializer(dish)
            serialized_data = serializer.data
            serialized_data['rate'] = recipe_rate(dish_id=serialized_data['id'])
            saved_recipe_list.append(serialized_data)
        return Response(saved_recipe_list)


class SavedRecipeDetailGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SavedRecipeDetailSerializer

    def get(self, request, pk):
        saved_recipe_detail = Dish.objects.get(id=pk)
        serializer = self.get_serializer(saved_recipe_detail)
        serialized_data = serializer.data
        serialized_data['author_name'] = User.objects.get(id=serialized_data['user_id']).first_name
        serialized_data['author_location'] = User.objects.get(id=serialized_data['user_id']).location
        serialized_data['rate'] = recipe_rate(pk)
        return Response(serialized_data)


class UnSaveRecipeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, pk):
        try:
            saved_recipe = SavedDish.objects.get(user_id=request.user, id=pk)
            saved_recipe.delete()
            return Response(status=204)
        except Exception as e:
            return Response({'message': str(e)}, status=400)
