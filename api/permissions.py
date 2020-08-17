from rest_framework.permissions import BasePermission
from django.conf import settings


class APIAuthentication(BasePermission):
    def has_permission(self, request, view):
        # API_KEY should be in request headers to authenticate requests
        api_key_secret = request.headers.get("Authorization")

        # Extract Key, last item, from "Bearer <api-key>"
        token = api_key_secret.split()[-1] if api_key_secret else None

        return token == settings.API_KEY
