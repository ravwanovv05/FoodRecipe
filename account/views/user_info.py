from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.views import get_user_model
from account.serializers.user_info_serializer import UserSerializer
User = get_user_model()


class UserInfoGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request):
        user = request.user
        user_serializer = self.get_serializer(user)
        return Response(user_serializer.data)
