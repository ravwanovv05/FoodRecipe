from django.urls import path
from users.views.authorization import RegisterGenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views.follow import FollowGenericAPIView, UnFollowGenericAPIView, FollowingUserGenericAPIView, \
    FollowersUserGenericAPIView
from users.views.personal_data import PersonalDataGenericAPIView
from users.views.user_info import UserInfoGenericAPIView

urlpatterns = [
    path('register', RegisterGenericAPIView.as_view(), name='register'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('follow', FollowGenericAPIView.as_view(), name='follow'),
    path('unfollow/<int:to_user>', UnFollowGenericAPIView.as_view(), name='unfollow'),
    path('following/<int:user_id>', FollowingUserGenericAPIView.as_view(), name='following'),
    path('followers/<int:user_id>', FollowersUserGenericAPIView.as_view(), name='followers'),
    path('personal-data', PersonalDataGenericAPIView.as_view(), name='personal-data'),
    path('user-info', UserInfoGenericAPIView.as_view(), name='user-info'),
]
