from django.urls import path
from .views.user_info import UserInfoAPIView

urlpatterns = [
    path('user-info', UserInfoAPIView.as_view(), name='user_info'),
]
