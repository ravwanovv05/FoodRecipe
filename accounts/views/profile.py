from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers.profile_serializer import ProfileSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from api.models.dish import Dish

User = get_user_model()


class ProfileGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProfileSerializer

    def get(self, request):
        profile = User.objects.get(id=request.user.id)
        serializer = self.get_serializer(profile)
        serialized_data = serializer.data
        serialized_data['recipe'] = Dish.objects.filter(user_id=request.user.id).count()
        return Response(serialized_data)
