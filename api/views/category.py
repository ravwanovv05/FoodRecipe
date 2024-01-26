from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from account.serializers.user import UserSerializer
from api.models.category import Category
from api.serializers.category import CategorySerializer
User = get_user_model()


class CategoryAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CategorySerializer

    def get(self, request):
        category = Category.objects.all()
        category_serializer = CategorySerializer(category, many=True)
        return Response({'Category data': category_serializer.data})
