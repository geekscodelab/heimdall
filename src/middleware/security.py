import logging

from django.contrib.auth.models import AnonymousUser
from knox.auth import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

_logger = logging.getLogger('heimdall.security')


class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user = None
        try:
            auth = TokenAuthentication()
            user, _ = auth.authenticate(request=request)
        except (TypeError, AuthenticationFailed):
            pass

        request.user = user or AnonymousUser()
        response = self.get_response(request)
        return response


class AuditLogMiddleware:
    """
    Audit log for all requests.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        username = request.user.username if request.user.username else 'anonymous'
        response = self.get_response(request)
        client_ip = request.META.get('REMOTE_ADDR')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0]

        _logger.info('{}@{} "{} {}" {}'.format(
            username,
            client_ip,
            request.method,
            request.get_full_path(),
            response.status_code
        ))
        return response
