from django.apps import AppConfig
from social_django.config import PythonSocialAuthConfig


class Auth0LoginConfig(AppConfig):
    name = 'auth0login'
    PythonSocialAuthConfig.default_auto_field = 'django.db.models.BigAutoField'
