from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Taxi API uchun yozilgan",
      default_version='v1',
      description="",
      contact= openapi.Contact("Amir Komilonov, Email: uchihasaske0102@gmail.com")

   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0)),
    path('user/', include('users.urls'))
]
