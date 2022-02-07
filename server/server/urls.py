from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from galaxynews.views import NewsViewSet

router = SimpleRouter()
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v0/base-auth', include('rest_framework.urls')),
    # path('api/v0/', include('galaxynews.urls')),
    path('api/v0/auth/', include('djoser.urls')),
    path('api/v0/auth-token', include('djoser.urls.authtoken')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls