from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pokedex.urls')),  # Importa las URLs de tu app "pokedex"
]
