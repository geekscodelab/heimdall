from rest_framework.routers import DefaultRouter

app_name = "users"
router = DefaultRouter()
router.include_root_view = False
urlpatterns = router.urls
