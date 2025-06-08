import requests
from django.shortcuts import render

API_BASE = "https://pokeapi.co/api/v2"

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

        return render(request, 'pokedex/detail.html', {
            'pokemon': pokemon,
            'types': types,
            'weaknesses': weaknesses
        })
    except:
        return render(request, 'pokedex/detail.html', {'error': f"No se encontró el Pokémon '{name}'."})

def compare_pokemon(request):
    result = None
    if request.method == 'POST':
        name1 = request.POST.get('pokemon1', '').lower()
        name2 = request.POST.get('pokemon2', '').lower()

        try:
            poke1 = requests.get(f"{API_BASE}/pokemon/{name1}/").json()
            poke2 = requests.get(f"{API_BASE}/pokemon/{name2}/").json()
            result = {
                'pokemon1': poke1,
                'pokemon2': poke2
            }
        except:
            result = None

    return render(request, 'pokedex/compare.html', {'result': result})
