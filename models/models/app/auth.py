from rest_framework import authentication
from rest_framework import exceptions
from .models import AuthenticationToken


class TokenAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTH", "")
        if not token:
            return None

        try:
            token_model = AuthenticationToken.objects.get(token=token)
        except AuthenticationToken.DoesNotExist:
            raise exceptions.AuthenticationFailed("Bad auth token")

        return (token_model.user, None)
