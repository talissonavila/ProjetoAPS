from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("theblog.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
