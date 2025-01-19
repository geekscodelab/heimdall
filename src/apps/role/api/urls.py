from rest_framework.routers import DefaultRouter

from apps.role.api.views import RoleViewSet

app_name = "roles"
router = DefaultRouter()
router.include_root_view = False
router.register("", RoleViewSet, basename="role")
urlpatterns = router.urls
