"""
Script para cargar datos de prueba en la base de datos.

Uso:
    python manage.py shell < populate_db.py

O desde el shell interactivo:
    python manage.py shell
    >>> exec(open('populate_db.py').read())
"""

import datetime
from publicaciones.models import Publicacion

# Limpia datos existentes para evitar duplicados
Publicacion.objects.all().delete()
print("🗑️  Base de datos limpia.")

# Datos de prueba
publicaciones_data = [
    {
        "titulo": "Introducción a las Class Based Views en Django",
        "autor": "Ana García",
        "contenido": (
            "Las Class Based Views (CBV) son una forma de definir vistas en Django "
            "usando clases de Python en lugar de funciones. Ofrecen reutilización de "
            "código mediante herencia y permiten separar la lógica por métodos HTTP "
            "(GET, POST, etc.). Django provee vistas genéricas como TemplateView, "
            "ListView y DetailView que cubren los casos más comunes sin necesidad de "
            "escribir lógica repetitiva."
        ),
        "fecha_publicacion": datetime.date(2026, 3, 10),
    },
    {
        "titulo": "El sistema de templates de Django",
        "autor": "Carlos López",
        "contenido": (
            "El lenguaje de templates de Django permite generar HTML dinámico desde "
            "el servidor. Sus principales características son: variables con {{ }}, "
            "etiquetas con {% %} y filtros con |. La herencia de templates mediante "
            "{% extends %} y {% block %} permite definir una estructura base y "
            "sobreescribir secciones específicas en cada página."
        ),
        "fecha_publicacion": datetime.date(2026, 3, 15),
    },
    {
        "titulo": "ListView y DetailView: vistas genéricas para modelos",
        "autor": "María Fernández",
        "contenido": (
            "ListView y DetailView son las CBV genéricas más usadas en Django. "
            "ListView obtiene automáticamente todos los objetos de un modelo y los "
            "pasa al template como una lista. DetailView obtiene un objeto específico "
            "por su clave primaria (pk) y lo pasa al template. Ambas soportan "
            "personalización mediante atributos como model, template_name, "
            "context_object_name y sobreescritura de get_queryset() o get_context_data()."
        ),
        "fecha_publicacion": datetime.date(2026, 3, 22),
    },
    {
        "titulo": "TemplateView: páginas estáticas con contexto dinámico",
        "autor": "Pedro Ramírez",
        "contenido": (
            "TemplateView es la CBV más simple de Django. Renderiza un template sin "
            "necesidad de un modelo. Es ideal para páginas de inicio, about, contacto "
            "o cualquier vista que no dependa de datos de base de datos. Para agregar "
            "variables al contexto se sobreescribe get_context_data(), llamando "
            "siempre a super() para no perder el contexto base de Django."
        ),
        "fecha_publicacion": datetime.date(2026, 4, 1),
    },
    {
        "titulo": "Namespaces de URLs en Django",
        "autor": "Laura Gómez",
        "contenido": (
            "El sistema de URLs de Django permite nombrar rutas y organizarlas en "
            "namespaces por app. Definiendo app_name en urls.py se puede usar "
            "{% url 'app:nombre' %} en templates y reverse('app:nombre') en vistas. "
            "Esto evita colisiones entre apps distintas que usen el mismo nombre de "
            "ruta y hace el código más mantenible cuando las URLs cambian."
        ),
        "fecha_publicacion": datetime.date(2026, 4, 10),
    },
    {
        "titulo": "Herencia de templates con extends y block",
        "autor": "Sofía Martínez",
        "contenido": (
            "La herencia de templates es uno de los mecanismos más potentes de "
            "Django. Un template base define la estructura HTML común (header, nav, "
            "footer) y declara bloques con {% block nombre %}{% endblock %}. Los "
            "templates hijos usan {% extends 'base.html' %} y sobreescriben solo "
            "los bloques que necesitan cambiar. Esto elimina la duplicación de HTML "
            "entre páginas."
        ),
        "fecha_publicacion": datetime.date(2026, 4, 18),
    },
    {
        "titulo": "get_object_or_404: manejo de errores en DetailView",
        "autor": "Diego Torres",
        "contenido": (
            "Cuando se solicita un objeto que no existe en la base de datos, Django "
            "puede devolver un error 500 genérico o un 404 informativo. DetailView "
            "maneja esto automáticamente: si el objeto no se encuentra, devuelve "
            "HTTP 404. También se puede usar get_object_or_404() en vistas "
            "personalizadas para el mismo efecto. Un 404 correcto mejora la "
            "experiencia del usuario y es importante para SEO."
        ),
        "fecha_publicacion": datetime.date(2026, 4, 25),
    },
    {
        "titulo": "El patrón MVT de Django",
        "autor": "Ana García",
        "contenido": (
            "Django implementa una variante del patrón MVC llamada MVT: Model, View, "
            "Template. El Model gestiona los datos y la lógica de negocio. La View "
            "recibe la request HTTP, consulta el modelo y devuelve una response. El "
            "Template define cómo presentar los datos en HTML. A diferencia de MVC "
            "clásico, en Django la 'vista' combina el rol del Controller y la View, "
            "mientras que el Template actúa como la View de MVC."
        ),
        "fecha_publicacion": datetime.date(2026, 5, 2),
    },
]

# Carga los datos
creadas = []
for data in publicaciones_data:
    pub = Publicacion.objects.create(**data)
    creadas.append(pub)
    print(f"  ✅ '{pub.titulo}' — {pub.autor} ({pub.fecha_publicacion})")

print(f"\n🎉 Se cargaron {len(creadas)} publicaciones correctamente.")
print("\nResumen:")
print(f"  Total en BD: {Publicacion.objects.count()} publicaciones")
print(f"  Autores únicos: {Publicacion.objects.values('autor').distinct().count()}")
print(f"  Más reciente: {Publicacion.objects.first()}")
print(f"  Más antigua:  {Publicacion.objects.last()}")