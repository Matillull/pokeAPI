import requests
from django.shortcuts import render

API_BASE = "https://pokeapi.co/api/v2"

# Diccionario con colores por tipo
TYPE_COLORS = {
    "fire": "#F08030",
    "water": "#6890F0",
    "grass": "#78C850",
    "electric": "#F8D030",
    "psychic": "#F85888",
    "ice": "#98D8D8",
    "dragon": "#7038F8",
    "dark": "#705848",
    "fairy": "#EE99AC",
    "normal": "#A8A878",
    "fighting": "#C03028",
    "flying": "#A890F0",
    "poison": "#A040A0",
    "ground": "#E0C068",
    "rock": "#B8A038",
    "bug": "#A8B820",
    "ghost": "#705898",
    "steel": "#B8B8D0"
}

def index(request):
    return render(request, 'pokedex/index.html')

def pokemon_detail(request, name):
    name = name.lower()
    pokemon_url = f"{API_BASE}/pokemon/{name}/"
    try:
        response = requests.get(pokemon_url)
        response.raise_for_status()
        pokemon = response.json()

        types = [t['type']['name'] for t in pokemon['types']]
        weaknesses = []

        if types:
            type_data = requests.get(f"{API_BASE}/type/{types[0]}/").json()
            weaknesses = [d['name'] for d in type_data['damage_relations']['double_damage_from']]
            
        # Obtener color de fondo según el primer tipo
            main_type = types[0] if types else "normal"
            bg_color = TYPE_COLORS.get(main_type, "#999999")

        return render(request, 'pokedex/detail.html', {
            'pokemon': pokemon,
            'types': types,
            'weaknesses': weaknesses,
            'bg_color': bg_color #Nuevo fragmento vinculado a los colores
        })
    except:
        return render(request, 'pokedex/detail.html', {'error': f"No se encontró el Pokémon '{name}'."})

def compare_pokemon(request):
    comparacion = []
    print("Comparación:", comparacion)

    if request.method == 'POST':
        name1 = request.POST.get('pokemon1', '').lower()
        name2 = request.POST.get('pokemon2', '').lower()

        for name in [name1, name2]:
            try:
                # Obtener datos básicos del Pokémon
                poke = requests.get(f"{API_BASE}/pokemon/{name}/").json()

                # Tipos
                types = [t['type']['name'] for t in poke['types']]

                # Debilidades
                weaknesses = []
                if types:
                    type_data = requests.get(f"{API_BASE}/type/{types[0]}/").json()
                    weaknesses = [d['name'] for d in type_data['damage_relations']['double_damage_from']]

                # Color de fondo según el tipo principal
                main_type = types[0] if types else "normal"
                bg_color = TYPE_COLORS.get(main_type, "#999999")

                # Agregar al listado de comparación
                comparacion.append({
                    'name': name,
                    'sprites': poke['sprites'],
                    'types': types,
                    'abilities': poke['abilities'],
                    'stats': poke['stats'],
                    'weaknesses': weaknesses,
                    'bg_color': bg_color,
                })

            except:
                pass  # Si un Pokémon falla, simplemente no lo agregamos

    return render(request, 'pokedex/compare.html', {'comparacion': comparacion})
