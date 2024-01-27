from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.models.dish import Dish
from api.models.saved_dish import SavedDish
from api.serializers.saved_recipe import SavedRecipeSerializer, SavedRecipeDetailSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class SavedRecipeGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SavedRecipeSerializer

    def get(self, request):
        saved_recipe = SavedDish.objects.filter(user_id=request.user.id)
        saved_recipe_list = []
        for sr in saved_recipe:
            dish = Dish.objects.get(id=sr.dish_id.id)
            saved_recipe_list.append(dish)
        serializer = self.get_serializer(saved_recipe_list, many=True)
        return Response(serializer.data)


class SavedRecipeDetailGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = SavedRecipeDetailSerializer

    def get(self, request, pk):
        print(pk)
        saved_recipe_detail = Dish.objects.get(id=pk)
        serializer = self.get_serializer(saved_recipe_detail)
        serialized_data = serializer.data
        print(serialized_data)
        serialized_data['author_name'] = User.objects.get(id=serialized_data['user_id']).first_name
        serialized_data['user_location'] = User.objects.get(id=serialized_data['user_id']).location
        return Response(serialized_data)


class UnSaveRecipeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        pass
