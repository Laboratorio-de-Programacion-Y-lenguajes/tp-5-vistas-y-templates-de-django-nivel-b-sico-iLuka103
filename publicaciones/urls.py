from django.urls import path
from . import views

# TODO: Asignar el namespace de la app.
# Esto permite usar {% url 'publicaciones:inicio' %} en los templates.
app_name = "publicaciones"

urlpatterns = [
    # TODO: Definir las tres rutas usando path() y .as_view()
    #
    # Rutas a implementar:
    #
    #   URL: ""
    #   Vista: InicioView
    #   Nombre: "inicio"
    #
    #   URL: "publicaciones/"
    #   Vista: PublicacionListView
    #   Nombre: "lista_publicaciones"
    #
    #   URL: "publicaciones/<int:publicacion_id>/"
    #   Vista: PublicacionDetailView
    #   Nombre: "detalle_publicacion"
    #
    # Pista para registrar una CBV:
    #   path("ruta/", views.MiVista.as_view(), name="nombre"),
]