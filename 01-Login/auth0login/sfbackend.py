from social_core.backends.salesforce import SalesforceOAuth2, SalesforceOAuth2Sandbox
from django.conf import settings

class Prod(SalesforceOAuth2):
    """Salesforce authentication backend"""
    # REDIRECT_STATE = False
    name = 'sf'
    OIDC_ENDPOINT = 'https://login.salesforce.com'


class Sandbox(SalesforceOAuth2Sandbox):
    name = 'sfsb'
    OIDC_ENDPOINT = 'https://test.salesforce.com'


class Custom(SalesforceOAuth2):
    name = 'sfc'
    AUTHORIZATION_URL = 'https://{}.my.salesforce.com/services/oauth2/authorize'.format(settings.OIDC_DOMAIN)
    ACCESS_TOKEN_URL = 'https://{}.my.salesforce.com/services/oauth2/token'.format(settings.OIDC_DOMAIN)
    REVOKE_TOKEN_URL = 'https://{}.my.salesforce.com/services/oauth2/revoke'.format(settings.OIDC_DOMAIN)
    OIDC_ENDPOINT = 'https://{}.my.salesforce.com'.format(settings.OIDC_DOMAIN)

