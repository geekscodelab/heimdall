from django.urls import include, path

app_name = "api_v1"
urlpatterns = [
    path(r"auth/", include("apps.auth.api.urls", namespace="auth")),
    path(r"permissions/", include("apps.permission.api.urls", namespace="permissions")),
    path(r"roles/", include("apps.role.api.urls", namespace="roles")),
    path(r"users/", include("apps.user.api.urls", namespace="users")),
]
