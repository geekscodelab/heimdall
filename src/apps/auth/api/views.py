from django.contrib.auth.signals import user_logged_in
from django.http import HttpRequest, HttpResponse
from knox.views import LoginView as KnoxLoginView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer


class LoginView(KnoxLoginView):
    """
    View to handle user login using Knox authentication.

    This view allows any user to log in by sending a POST request with valid credentials.
    """

    permission_classes = (permissions.AllowAny,)

    def post(self, request: HttpRequest) -> HttpResponse:
        """
        Handle POST request to log in a user.

        Args:
            request (HttpRequest): The incoming HTTP request.

        Returns:
            HttpResponse: The HTTP response after logging in the user.

        """
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        request.user = user
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return super().post(request)
