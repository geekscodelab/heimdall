import logging

from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest, HttpResponse
from knox.auth import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

_logger = logging.getLogger("heimdall.security")


class AuthenticationMiddleware:
    """
    Middleware that authenticates users for incoming requests.
    """

    def __init__(self, get_response: HttpResponse) -> None:
        """
        Initialize the middleware with the given response handler.

        Args:
            get_response (HttpResponse): The response handler.

        """
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """
        Process the request, authenticate the user, and return the response.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The HTTP response.

        """
        user = None
        try:
            auth = TokenAuthentication()
            user, _ = auth.authenticate(request=request)
        except (TypeError, AuthenticationFailed):
            pass

        request.user = user or AnonymousUser()
        return self.get_response(request)


class AuditLogMiddleware:
    """
    Middleware that logs audit information for all incoming requests.
    """

    def __init__(self, get_response: HttpResponse) -> None:
        """
        Initialize the middleware with the given response handler.

        Args:
            get_response (HttpResponse): The response handler.

        """
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """
        Process the request, log audit information, and return the response.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The HTTP response.

        """
        username = request.user.username if request.user.username else "anonymous"
        response = self.get_response(request)
        client_ip = request.META.get("REMOTE_ADDR")
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(",")[0]

        msg = f'{username}@{client_ip} "{request.method} {request.get_full_path()}" {response.status_code}'
        _logger.info(msg)
        return response
