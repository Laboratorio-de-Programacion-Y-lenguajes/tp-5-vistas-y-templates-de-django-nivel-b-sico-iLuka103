import datetime
from django.test import TestCase
from django.urls import reverse
from publicaciones.models import Publicacion


class InicioViewTest(TestCase):
    """Tests para InicioView (TemplateView)."""

    def test_inicio_responde_200(self):
        response = self.client.get(reverse("publicaciones:inicio"))
        self.assertEqual(response.status_code, 200)

    def test_inicio_usa_template_correcto(self):
        response = self.client.get(reverse("publicaciones:inicio"))
        self.assertTemplateUsed(response, "publicaciones/inicio.html")

    def test_inicio_usa_base_template(self):
        response = self.client.get(reverse("publicaciones:inicio"))
        self.assertTemplateUsed(response, "base.html")

    def test_inicio_contexto_tiene_titulo(self):
        response = self.client.get(reverse("publicaciones:inicio"))
        self.assertIn("titulo", response.context)

    def test_inicio_contexto_tiene_mensaje(self):
        response = self.client.get(reverse("publicaciones:inicio"))
        self.assertIn("mensaje", response.context)


class PublicacionListViewTest(TestCase):
    """Tests para PublicacionListView (ListView)."""

    def setUp(self):
        self.pub1 = Publicacion.objects.create(
            titulo="Primera publicación",
            autor="Ana García",
            contenido="Contenido de la primera publicación.",
            fecha_publicacion=datetime.date(2026, 3, 10),
        )
        self.pub2 = Publicacion.objects.create(
            titulo="Segunda publicación",
            autor="Carlos López",
            contenido="Contenido de la segunda publicación.",
            fecha_publicacion=datetime.date(2026, 3, 15),
        )

    def test_lista_responde_200(self):
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertEqual(response.status_code, 200)

    def test_lista_usa_template_correcto(self):
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertTemplateUsed(response, "publicaciones/publicacion_list.html")

    def test_lista_usa_base_template(self):
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertTemplateUsed(response, "base.html")

    def test_lista_contexto_tiene_publicacion_list(self):
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertIn("publicacion_list", response.context)

    def test_lista_contiene_ambas_publicaciones(self):
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertEqual(len(response.context["publicacion_list"]), 2)

    def test_lista_vacia_responde_200(self):
        Publicacion.objects.all().delete()
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertEqual(response.status_code, 200)


class PublicacionDetailViewTest(TestCase):
    """Tests para PublicacionDetailView (DetailView)."""

    def setUp(self):
        self.pub = Publicacion.objects.create(
            titulo="Publicación de detalle",
            autor="María Fernández",
            contenido="Contenido completo para el detalle.",
            fecha_publicacion=datetime.date(2026, 4, 1),
        )

    def test_detalle_responde_200(self):
        url = reverse(
            "publicaciones:detalle_publicacion",
            kwargs={"publicacion_id": self.pub.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detalle_id_inexistente_responde_404(self):
        url = reverse(
            "publicaciones:detalle_publicacion",
            kwargs={"publicacion_id": 99999},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_detalle_usa_template_correcto(self):
        url = reverse(
            "publicaciones:detalle_publicacion",
            kwargs={"publicacion_id": self.pub.pk},
        )
        response = self.client.get(url)
        self.assertTemplateUsed(response, "publicaciones/publicacion_detail.html")

    def test_detalle_usa_base_template(self):
        url = reverse(
            "publicaciones:detalle_publicacion",
            kwargs={"publicacion_id": self.pub.pk},
        )
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")

    def test_detalle_contexto_tiene_publicacion(self):
        url = reverse(
            "publicaciones:detalle_publicacion",
            kwargs={"publicacion_id": self.pub.pk},
        )
        response = self.client.get(url)
        self.assertIn("publicacion", response.context)

    def test_detalle_publicacion_en_contexto_es_correcta(self):
        url = reverse(
            "publicaciones:detalle_publicacion",
            kwargs={"publicacion_id": self.pub.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.context["publicacion"], self.pub)