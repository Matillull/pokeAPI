import httpx
from django.shortcuts import render
from django.http import JsonResponse

# URL base de la PokéAPI
API_BASE = "https://pokeapi.co/api/v2"

# Colores por tipo para usar en las tarjetas
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

# Obtiene los datos completos de un Pokémon desde la API
async def fetch_pokemon_data(name):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE}/pokemon/{name}/")
        response.raise_for_status()
        return response.json()

# Obtiene información del tipo (para sacar debilidades)
async def fetch_type_data(type_name):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE}/type/{type_name}/")
        response.raise_for_status()
        return response.json()

# Página principal
async def index(request):
    return render(request, 'pokedex/index.html')

# Vista para ver los detalles de un Pokémon
async def pokemon_detail(request, name):
    name = name.lower()
    try:
        pokemon = await fetch_pokemon_data(name)
        types = [t['type']['name'] for t in pokemon['types']]
        weaknesses = []
        bg_color = "#999999"

        if types:
            type_data = await fetch_type_data(types[0])
            weaknesses = [d['name'] for d in type_data['damage_relations']['double_damage_from']]
            main_type = types[0]
            bg_color = TYPE_COLORS.get(main_type, "#999999")

        return render(request, 'pokedex/detail.html', {
            'pokemon': pokemon,
            'types': types,
            'weaknesses': weaknesses,
            'bg_color': bg_color
        })
    except httpx.HTTPStatusError:
        return render(request, 'pokedex/detail.html', {
            'error': f"No se encontró el Pokémon '{name}'."
        })

# Vista para comparar dos Pokémon
async def compare_pokemon(request):
    comparacion = []

    if request.method == 'POST':
        name1 = request.POST.get('pokemon1', '').lower()
        name2 = request.POST.get('pokemon2', '').lower()

        for name in [name1, name2]:
            try:
                poke = await fetch_pokemon_data(name)
                types = [t['type']['name'] for t in poke['types']]
                weaknesses = []

                if types:
                    type_data = await fetch_type_data(types[0])
                    weaknesses = [d['name'] for d in type_data['damage_relations']['double_damage_from']]

                main_type = types[0] if types else "normal"
                bg_color = TYPE_COLORS.get(main_type, "#999999")

                comparacion.append({
                    'name': name,
                    'sprites': poke['sprites'],
                    'types': types,
                    'abilities': poke['abilities'],
                    'stats': poke['stats'],
                    'weaknesses': weaknesses,
                    'bg_color': bg_color,
                })
            except httpx.HTTPStatusError:
                continue

    return render(request, 'pokedex/compare.html', {'comparacion': comparacion})

# API JSON para obtener datos completos de un Pokémon
async def api_pokemon_detail(request, name):
    try:
        pokemon = await fetch_pokemon_data(name)
        types = [t['type']['name'] for t in pokemon['types']]
        weaknesses = []
        bg_color = "#999999"

        if types:
            type_data = await fetch_type_data(types[0])
            weaknesses = [d['name'] for d in type_data['damage_relations']['double_damage_from']]
            main_type = types[0]
            bg_color = TYPE_COLORS.get(main_type, "#999999")

        return JsonResponse({
            'success': True,
            'data': {
                'pokemon': pokemon,
                'types': types,
                'weaknesses': weaknesses,
                'bg_color': bg_color
            }
        })
    except httpx.HTTPStatusError as e:
        return JsonResponse({
            'success': False,
            'error': f"No se encontró el Pokémon '{name}'",
            'status_code': e.response.status_code
        }, status=404)

# API para autocompletado: devuelve lista de nombres de Pokémon
async def api_pokemon_list(request):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{API_BASE}/pokemon?limit=1000")
        response.raise_for_status()
        data = response.json()
        return JsonResponse([p['name'] for p in data['results']], safe=False)
