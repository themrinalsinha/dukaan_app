from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from rest_framework.response import Response

from seller.models import SellerAccount
from buyer.models import CustomerAccount


class SellerAuth(BaseAuthentication):
    def authenticate(self, request):
        reason = "Invalid Authorization header"

        if "HTTP_AUTHORIZATION" in request.META:
            auth = request.META["HTTP_AUTHORIZATION"].split()
            if len(auth) == 2 and auth[0].upper() == "DUKAAN":
                _, _token = auth
                instance = SellerAccount.objects.filter(auth_token=_token).first()
                if instance:
                    request.account = instance
                    return None

        raise AuthenticationFailed(reason)


class BuyerAuth(BaseAuthentication):
    def authenticate(self, request):

        if "HTTP_AUTHORIZATION" in request.META:
            auth = request.META["HTTP_AUTHORIZATION"].split()
            if len(auth) == 2 and auth[0].upper() == "DUKAAN":
                _, _token = auth
                instance = CustomerAccount.objects.filter(auth_token=_token).first()
                if instance:
                    request.account = instance
                    return None
                else:
                    raise AuthenticationFailed("Invalid Token")

        elif "HTTP_COOKIE" in request.META:
            session = request.META["HTTP_COOKIE"]
            request.unauthorized_account = session
            return None

        elif "REMOTE_ADDR" in request.META:
            remote = request.META["REMOTE_ADDR"]
            request.unauthorized_account = remote
            return None

        else:
            raise AuthenticationFailed("Something went wrong...")
