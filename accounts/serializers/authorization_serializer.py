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
    token = CharField(min_length=1, write_only=True)
    uidb64 = CharField(min_length=1, write_only=True)

    class Meta:
        fields = ('password', 'token', 'uidb64')

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is invalid', 401)
            user.set_password(password)
            user.save()
        except Exception as e:
            raise AuthenticationFailed('The reset link is invalid', 401)
        return super().validate(attrs)