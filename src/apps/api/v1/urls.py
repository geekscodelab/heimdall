from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Heimdall API",
        default_version='v1',
        description="Heimdall API documentation - authentication and authorization",
        contact=openapi.Contact(email=""),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'api_v1'
urlpatterns = [
    path(r'auth/', include('apps.auth.api.urls', namespace='auth')),
    path(r'permissions/', include('apps.permission.api.urls', namespace='permissions')),
    path(r'groups/', include('apps.group.api.urls', namespace='groups')),
    path(r'users/', include('apps.user.api.urls', namespace='users')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
