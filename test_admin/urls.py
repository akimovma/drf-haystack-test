from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from test_admin import settings
from apps.users.views import UserViewSet
from apps.categories.views import CategoryViewSet
from .views import GlobalSearchViewSet


router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'search', GlobalSearchViewSet, base_name='search')

urlpatterns = [url(r'^admin/', admin.site.urls),
               url(r'^api/', include(router.urls, namespace='api')),
               url(r'^api/auth/login/', obtain_jwt_token),
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns.append(url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')))
