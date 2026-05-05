from django.db import models


class Publicacion(models.Model):
    """
    Representa una publicación del portal.

    Atributos:
        titulo (str): Título de la publicación.
        autor (str): Nombre del autor.
        contenido (str): Texto completo de la publicación.
        fecha_publicacion (date): Fecha en que fue publicada.
    """

    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()

    class Meta:
        ordering = ["-fecha_publicacion"]
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return self.titulo