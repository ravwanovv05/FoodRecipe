from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api.models.comment import Comment
from api.serializers.comment_serializer import CommentSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentRecipeGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)


class CommentsRecipeGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def get(self, request, dish_id):
        comments = Comment.objects.filter(dish_id=dish_id)
        serializer = self.get_serializer(comments, many=True)
        serialized_data = serializer.data
        for data in serialized_data:
            data['user_name'] = User.objects.get(id=data['user_id']).first_name
            try:
                data['user_avatar'] = User.objects.get(id=data['user_id']).avatar.url
            except:
                data['user_avatar'] = None
        return Response(serializer.data)

