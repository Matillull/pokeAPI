from django.urls import path
from . import views

urlpatterns = [
    # Página principal (index)
    path('', views.index, name='index'),

    # Detalles de un Pokémon por nombre
    path('pokemon/<str:name>/', views.pokemon_detail, name='pokemon_detail'),

    # Vista para comparar dos Pokémon (GET muestra formulario, POST procesa)
    path('compare/', views.compare_pokemon, name='compare'),

    # API JSON: detalles de un Pokémon específico
    path('api/pokemon/<str:name>/', views.api_pokemon_detail, name='api_pokemon_detail'),

    # API JSON: lista de todos los nombres de Pokémon (para autocompletado)
    path('api/pokemon-list/', views.api_pokemon_list, name='api_pokemon_list'),
]
