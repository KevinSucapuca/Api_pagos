from django.contrib import admin
from django.urls import path, include,re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Documentación del API Pago de servicios",
        default_version='v1',
        description="Proyecto API de Silabuz",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ksucapuca007@gmail.com"),
        license=openapi.License(name="BSD License"), 
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('v1.urls')),
    path("users/", include("page.urls")),
    re_path(r"^api/v1/", include("v1.urls")),
    #re_path(r"^api/v2/", include("v2.urls")),

    # Documentacion de mi proyecto
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),

    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),

    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),

]