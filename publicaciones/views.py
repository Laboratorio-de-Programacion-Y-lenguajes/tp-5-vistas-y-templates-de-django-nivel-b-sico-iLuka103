from django.views.generic import TemplateView, ListView, DetailView
from .models import Publicacion
    
class InicioView(TemplateView):
    template_name = "publicaciones/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Publicaciones"
        context["mensaje"] = "BIENVENIDOO"
        return context

class PublicacionListView(ListView):
        model = Publicacion
        template_name = "publicaciones/publicacion_list.html"
        context_object_name = "publicacion_list"


class PublicacionDetailView(DetailView): 
        model = Publicacion
        template_name = "publicaciones/publicacion_detail.html"
        context_object_name = "publicacion"
        pk_url_kwarg = "publicacion_id"