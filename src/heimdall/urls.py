from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path(r'api/v1/', include('apps.api.v1.urls', namespace='api_v1')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
