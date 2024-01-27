from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from api.models.dish import Dish
from api.serializers.search_recipe import SearchRecipeSerializer


class SearchRecipeAPIView(ListAPIView):
    authentication_classes = ()
    permission_classes = ()
    queryset = Dish.objects.all()
    serializer_class = SearchRecipeSerializer
    filter_backends = (SearchFilter,)
    search_fields = ['name']
