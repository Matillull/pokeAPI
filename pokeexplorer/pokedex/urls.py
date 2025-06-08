from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokemon/<str:name>/', views.pokemon_detail, name='pokemon_detail'),
    path('compare/', views.compare_pokemon, name='compare'),
]
