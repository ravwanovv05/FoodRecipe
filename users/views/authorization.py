from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from users.serializers.authorization_serializer import RegisterSerializer

User = get_user_model()


class RegisterGenericAPIView(GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        confirm_password = request.data['confirm_password']
        if password != confirm_password:
            return Response({'message': 'Passwords do not match'}, status=400)

        if User.objects.filter(email=email).exists():
            return Response({'message': 'Email already exists'}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
