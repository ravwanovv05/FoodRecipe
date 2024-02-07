from django.urls import path
from accounts.views.authorization import RegisterGenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from accounts.views.follow import FollowGenericAPIView, UnFollowGenericAPIView, \
    FollowingUserGenericAPIView, FollowersUserGenericAPIView
from accounts.views.personal_data import PersonalDataGenericAPIView
from accounts.views.user_info import UserInfoGenericAPIView
from .views.google_facebook_login import ( GoogleLogin, callback_google, RedirectToGoogleAPIView,
                    FacebookLogin, RedirectToFacebookApiView, callback_facebook)
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

    # Google
    path('google', GoogleLogin.as_view(), name='google_login'),
    path('google-login', RedirectToGoogleAPIView.as_view(), name='google_login2'),
    path('google/callback', callback_google, name='google_callback'),
    # Facebook
    path('facebook', FacebookLogin.as_view(), name='facebook'),
    path('facebook-login', RedirectToFacebookApiView.as_view(), name='facebook-login'),
    path('facebook/callback', callback_facebook, name='facebook_callback')
]

