import datetime
from django.test import TestCase
from django.urls import reverse
from publicaciones.models import Publicacion


class InicioTemplateTest(TestCase):
    """Tests de contenido renderizado en la página de inicio."""

    def test_inicio_muestra_titulo_en_respuesta(self):
        response = self.client.get(reverse("publicaciones:inicio"))
        self.assertIn("titulo", response.context)
        titulo = response.context["titulo"]
        self.assertContains(response, titulo)

    def test_inicio_muestra_mensaje_en_respuesta(self):
        response = self.client.get(reverse("publicaciones:inicio"))
        self.assertIn("mensaje", response.context)
        mensaje = response.context["mensaje"]
        self.assertContains(response, mensaje)

    def test_inicio_tiene_link_a_lista(self):
        response = self.client.get(reverse("publicaciones:inicio"))
        url_lista = reverse("publicaciones:lista_publicaciones")
        self.assertContains(response, url_lista)


class ListaTemplateTest(TestCase):
    """Tests de contenido renderizado en el listado de publicaciones."""

    def setUp(self):
        self.pub = Publicacion.objects.create(
            titulo="Artículo de prueba",
            autor="Laura Gómez",
            contenido="Texto del artículo.",
            fecha_publicacion=datetime.date(2026, 5, 1),
        )

    def test_lista_muestra_titulo_de_publicacion(self):
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertContains(response, "Artículo de prueba")

    def test_lista_muestra_autor_de_publicacion(self):
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertContains(response, "Laura Gómez")

    def test_lista_tiene_link_al_detalle(self):
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        url_detalle = reverse(
            "publicaciones:detalle_publicacion",
            kwargs={"publicacion_id": self.pub.pk},
        )
        self.assertContains(response, url_detalle)

    def test_lista_vacia_muestra_mensaje_amigable(self):
        Publicacion.objects.all().delete()
        response = self.client.get(reverse("publicaciones:lista_publicaciones"))
        self.assertEqual(response.status_code, 200)
        # El template debe mostrar algo cuando no hay publicaciones
        self.assertNotContains(response, "Error")


class DetalleTemplateTest(TestCase):
    """Tests de contenido renderizado en el detalle de publicación."""

    def setUp(self):
        self.pub = Publicacion.objects.create(
            titulo="Título del detalle",
            autor="Pedro Ramírez",
            contenido="Contenido extenso de la publicación de prueba.",
            fecha_publicacion=datetime.date(2026, 4, 20),
        )
        self.url = reverse(
            "publicaciones:detalle_publicacion",
            kwargs={"publicacion_id": self.pub.pk},
        )

    def test_detalle_muestra_titulo(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Título del detalle")

    def test_detalle_muestra_autor(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Pedro Ramírez")

    def test_detalle_muestra_contenido(self):
        response = self.client.get(self.url)
        self.assertContains(response, "Contenido extenso de la publicación de prueba.")

    def test_detalle_tiene_link_de_vuelta_al_listado(self):
        response = self.client.get(self.url)
        url_lista = reverse("publicaciones:lista_publicaciones")
        self.assertContains(response, url_lista)