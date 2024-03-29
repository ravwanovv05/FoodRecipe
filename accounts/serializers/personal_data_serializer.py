from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class PersonalDataSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'avatar', 'bio', 'location')
