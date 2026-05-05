from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # TODO: Incluir las rutas de la app publicaciones usando include()
    # Pista: path("", include("publicaciones.urls")),
]