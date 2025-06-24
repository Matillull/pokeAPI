from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ruta del panel de administración de Django
    path('admin/', admin.site.urls),

    # Incluye las rutas de la app 'pokedex'
    path('', include('pokedex.urls')),
]
