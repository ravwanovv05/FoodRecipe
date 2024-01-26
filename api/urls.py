from django.urls import path
from api.views.dish import CreateDishGenericAPIView

urlpatterns = [
    path('create-dish', CreateDishGenericAPIView.as_view(), name='create-dish'),
]
