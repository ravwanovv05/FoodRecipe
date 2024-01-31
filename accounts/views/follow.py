from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from accounts.models.user_follow import UserFollow
from accounts.serializers.follow_serializer import FollowSerializer, FollowingFollowersSerializer
from accounts.user_utils.increment_decremet import increment, decrement

User = get_user_model()


class FollowGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        increment(from_user=request.user.id, to_user=serializer.data['to_user'])
        return Response(serializer.data, status=200)


class UnFollowGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def delete(self, request, to_user):
        follow_user = UserFollow.objects.get(from_user=request.user.id)
        decrement(from_user=request.user.id, to_user=to_user)
        follow_user.delete()
        return Response(status=204)


class FollowingUserGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowingFollowersSerializer

    def get(self, request, user_id):
        following_users = UserFollow.objects.filter(from_user=user_id)
        data_list = []
        for following_user in following_users:
            user = User.objects.get(pk=following_user.to_user.pk)
            serializer = self.get_serializer(user)
            data_list.append(serializer.data)
        return Response(data_list, status=200)


class FollowersUserGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowingFollowersSerializer

    def get(self, request, user_id):
        following_users = UserFollow.objects.filter(to_user=user_id)
        data_list = []
        for follow_user in following_users:
            user = User.objects.get(pk=follow_user.from_user.pk)
            serializer = self.get_serializer(user)
            data_list.append(serializer.data)
        return Response(data_list, status=200)

