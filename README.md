# PokeExplorer

Este proyecto es una aplicación web construida con Django que consume la API de PokéAPI para mostrar información de Pokémon. Incluye un buscador y estilos con Bootstrap.

## Diseño del sistema y tecnologías utilizadas

-**Frontend**: HTML, CSS, Bootstrap
-**Programación**: Django
-**Consumo de API REST**: PokéApi (`https://pokeapi.co/api/v2`)
-**Diseño visual**: Utilizando cómo ejemplo los colores característicos de Pokemón y la página de PokéAPI
-**Gestión de vistas**:
	-Página de inicio con buscador
	-Página de detalles del Pokemón
	-Página de comparación Pokemón
	-Página Q&A (estática)

## 🚀 Requisitos

- Python 3.10 o superior
- pip (viene con Python)
- Git (opcional pero recomendado)

## 🧱 Instalación

1. **Clonar el repositorio:**


git clone https://github.com/Matillull/pokeAPI.git
cd pokeAPI

2. **Crear y activar un entorno virtual (opcional pero recomendado):**

python -m venv venv
venv\Scripts\activate


Linux/Mac (no testeado): 
python3 -m venv venv
source venv/bin/activate

3. **Instalar dependencias:**
pip install -r requirements.txt

USO:
1. Ejecutar las migraciones
python manage.py migrate

2. Ejectuar Servidor
python manage.py runserver

3. Abrir el navegador en la URL que sale en terminal


## Mockups y Mapa de navegación

**Mockups**

#### Página de Inicio
![Mockup Inicio](pokedex/mockups/index.png)

#### Página de Detalles
![Mockup Detalles](pokedex/mockups/detail.png)

#### Comparar Pokémon
![Mockup Comparar](pokedex/mockups/compare.png)

**Mapa de navegación**

[Inicio]
   ↓ buscar Pokémon
   ↓ comparar Pokémon
[Detalles del Pokémon]
   ↳ volver al inicio

[Comparar Pokémon]
   ↳ elegir dos Pokémon → ver tabla comparativa

[Q&A]
   ↳ acceso desde navbar (sin funcionalidad activa)
   

##Interacción y retroalimentación

**El usuario puede:**

-Buscar un Pokemón -> Se muestra una tarjeta con el nombre del Pokemón, una foto respectiva del mismo y sus características
-Comparar Pokemón -> El usuario puede ingresar dos Pokemón para conocer las estadísticas de ambos y eso ayudarlo a comparar entre ellos
-Navegar entre secciones -> Mediante un navbar

**Cada acción ofrece retroalimentación visual:**

-Mensajes claros si no se encuentra el Pokemón
-Tabla inmediata al buscar el Pokemón
-Ofrece la posibilidad de comparar Pokemón incluso al momento de buscar uno


##Servicios REST utilizados

La aplicación consume los datos de la PokéAPI desde el backend, utilizando el módulo requests de Python en las vistas de Django.
Las principales rutas REST utilizadas son:

GET /pokemon/{nombre}: para obtener información general del Pokémon (imagen, tipos, estadísticas, etc.)

GET /type/{tipo}: para obtener información sobre debilidades (relaciones de daño)

Las vistas procesan esta información en el servidor y la pasan a las plantillas HTML para ser renderizada dinámicamente, evitando que el cliente realice llamadas directas a la API externa.
