from django.views.generic import TemplateView, ListView, DetailView
from .models import Publicacion

# ---------------------------------------------------------------------------
# InicioView
# ---------------------------------------------------------------------------
# TODO: Implementar InicioView usando TemplateView.
#
# Requisitos:
#   - template_name = "publicaciones/inicio.html"
#   - Sobreescribir get_context_data() para agregar al contexto:
#       "titulo"  → str con el nombre del portal
#       "mensaje" → str de bienvenida
#
# Pista:
#   class InicioView(TemplateView):
#       template_name = "..."
#
#       def get_context_data(self, **kwargs):
#           context = super().get_context_data(**kwargs)
#           context["titulo"] = "..."
#           context["mensaje"] = "..."
#           return context
    
class InicioView(TemplateView):
        template_name = "publicaciones/inicio.html"

        def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["titulo"] = "Publicaciones"
                context["mensaje"] = "BIENVENIDO"
                return context

# ---------------------------------------------------------------------------
# PublicacionListView
# ---------------------------------------------------------------------------
# TODO: Implementar PublicacionListView usando ListView.
#
# Requisitos:
#   - model = Publicacion
#   - context_object_name = "publicacion_list"
#     (el template accede a esta variable con {% for pub in publicacion_list %})
#
# Pista:
#   class PublicacionListView(ListView):
#       model = ...
#       context_object_name = "..."

class PublicacionListView(ListView):
    model = Publicacion
    template_name = "publicaciones/publicacion_list.html"
    context_object_name = "publicacion_list"


# ---------------------------------------------------------------------------
# PublicacionDetailView
# ---------------------------------------------------------------------------
# TODO: Implementar PublicacionDetailView usando DetailView.
#
# Requisitos:
#   - model = Publicacion
#   - context_object_name = "publicacion"
#     (el template accede a esta variable con {{ publicacion.titulo }})
#   - pk_url_kwarg = "publicacion_id"
#     (indica que el parámetro en la URL se llama "publicacion_id", no "pk")
#   - Si no existe la publicación → responde automáticamente con 404
#
# Pista:
#   class PublicacionDetailView(DetailView):
#       model = ...
#       context_object_name = "..."
#       pk_url_kwarg = "..."

    class PublicacionDetailView(DetailView): 
        model = Publicacion
        template_name = "publicaciones/publicacion_detail.html"
        context_object_name = "publicacion"
        pk_url_kwarg = "publicacion_id"