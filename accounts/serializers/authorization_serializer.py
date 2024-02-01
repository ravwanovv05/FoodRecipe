from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import CharField, EmailField
from rest_framework.serializers import ModelSerializer, Serializer
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(ModelSerializer):
    confirm_password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password', 'confirm_password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            first_name=validated_data['first_name'],
            email=validated_data['email'],
            username=None,
            password=validated_data['password']
        )
        return user


class PasswordResetEmailSerializer(Serializer):
    email = EmailField(min_length=2)

    class Meta:
        fields = ('email',)


class SetNewPasswordSerializer(Serializer):
    password = CharField(min_length=6, max_length=68, write_only=True)
    confirm_password = CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        fields = ('password', 'confirm_password')

