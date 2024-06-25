from rest_framework_simplejwt import authentication as jwt_authentication
from django.conf import settings
from rest_framework import authentication, exceptions as rest_exceptions


class CSRFCheck:
    def __init__(self, request):
        self.request = request

    def enforce_csrf(self):
        check = authentication.CSRFCheck(self.request)
        reason = check.process_view(self.request, None, (), {})
        if reason:
            raise rest_exceptions.PermissionDenied('CSRF Failed: %s' % reason)


class CustomAuthentication(jwt_authentication.JWTAuthentication):
    def authenticate(self, request):
        raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])

        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)

        csrf_checker = CSRFCheck(request)
        csrf_checker.enforce_csrf()

        return (self.get_user(validated_token), validated_token)
