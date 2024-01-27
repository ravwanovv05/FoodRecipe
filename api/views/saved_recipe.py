from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated


class SavedRecipeGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ''