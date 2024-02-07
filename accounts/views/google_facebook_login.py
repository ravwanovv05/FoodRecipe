import os
import requests
from allauth.socialaccount.models import SocialApp
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.views import get_user_model
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView

User = get_user_model()


class RedirectToGoogleAPIView(APIView):

    def get(self, request):
        google_redirect_uri = os.getenv('GOOGLE_REDIRECT_URI')
        try:
            google_client_id = SocialApp.objects.get(provider='google').client_id
        except SocialApp.DoesNotExist:
            return Response({'success': False, 'message': 'SocialApp does not exist'}, status=404)
        url = f'https://accounts.google.com/o/oauth2/v2/auth?redirect_uri={google_redirect_uri}&prompt=consent&response_type=code&client_id={google_client_id}&scope=openid email profile&access_type=offline'
        return redirect(url)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = 'https://8830-178-218-201-17.ngrok-free.app/accounts/google/callback'
    client_class = OAuth2Client


@api_view(["GET"])
def callback_google(request):
    """Callback"""
    code = request.GET.get("code")
    res = requests.post("https://8830-178-218-201-17.ngrok-free.app/accounts/google", data={"code": code}, timeout=30)
    return Response(res.json())


# Facebook sign-in
class RedirectToFacebookApiView(APIView):
    def get(self, request):
        facebook_redirect_uri = os.getenv('FACEBOOK_REDIRECT_URI')
        facebook_app_id = os.getenv('FACEBOOK_APP_ID')
        try:
            url = f'https://www.facebook.com/v9.0/dialog/oauth?client_id={facebook_app_id}&redirect_uri={facebook_redirect_uri}&scope=email,public_profile'
        except SocialApp.DoesNotExist:
            return Response({'success': False, 'message': 'Social does not exist'}, status=404)
        return redirect(url)


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    callback_url = "https://8830-178-218-201-17.ngrok-free.app/accounts/facebook/callback_facebook"
    client_class = OAuth2Client


@api_view(['GET'])
def callback_facebook(request):
    """Callback function to handle the Facebook OAuth2 callback."""
    code = request.query_params.get('code')
    if not code:
        return Response({'error': 'Code parameter is missing.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = requests.get("https://graph.facebook.com/v9.0/oauth/access_token", params={
            'client_id': os.getenv('FACEBOOK_APP_ID'),
            'redirect_uri': os.getenv('FACEBOOK_REDIRECT_URI'),
            'client_secret': os.getenv('FACEBOOK_APP_SECRET'),
            'code': code,
        })

        response.raise_for_status()
        data = response.json()
        access_token = data.get('access_token')

        if access_token:
            user_info_response = requests.get("https://graph.facebook.com/me", params={
                'fields': 'id,name,email',
                'access_token': access_token,
            })
            user_info_response.raise_for_status()
            user_info = user_info_response.json()

            return Response({'access_token': access_token, 'user_info': user_info}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Access token not found.'}, status=status.HTTP_400_BAD_REQUEST)
    except requests.exceptions.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
