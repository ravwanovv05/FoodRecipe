from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from api.serializers.dish_crud import CreateDishSerializer


class CreateDishGenericAPIView(GenericAPIView):
    permission_classes = IsAuthenticated
    serializer_class = CreateDishSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

