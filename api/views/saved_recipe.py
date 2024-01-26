from drf_yasg.openapi import Response
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from api.models.dish import Dish
from api.models.saved_dish import SavedDish
from api.serializers.saved_recipe import SavedRecipeSerializer


class SavedRecipeGenericAPIView(GenericAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = SavedRecipeSerializer

    def get(self, request):
        saved_recipe = SavedDish.objects.filter(user_id=request.user.id)
        saved_recipe_list = []
        for sr in saved_recipe:
            dish = Dish.objects.get(id=sr.dish_id)
            # serializer = self.get_serializer(data=dish)
            saved_recipe_list.append(dish)
        serializer = self.get_serializer(data=saved_recipe_list, many=True)
        return Response(serializer.data)

