import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Directorio actual donde está main.py
current_dir = os.path.dirname(os.path.abspath(__file__))

# Rutas completas
static_dir = os.path.join(current_dir, "static")
templates_dir = os.path.join(current_dir, "templates")

app.mount("/static", StaticFiles(directory=static_dir), name="static")
templates = Jinja2Templates(directory=templates_dir)

# Configurar el directorio de templates
templates = Jinja2Templates(directory="templates")

# Ruta principal que sirve el HTML con el mapa
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"titulo": "Mapa Mundial Interactivo"}
    )

# Ruta adicional con parámetros (ejemplo)
@app.get("/mapa/{ciudad}", response_class=HTMLResponse)
async def mapa_ciudad(request: Request, ciudad: str):
    # Puedes pasar datos dinámicos al template
    ciudades = {
        "madrid": {"lat": 40.4168, "lng": -3.7038},
        "londres": {"lat": 51.5074, "lng": -0.1278},
        "tokio": {"lat": 35.6762, "lng": 139.6503}
    }
    
    coordenadas = ciudades.get(ciudad.lower(), {"lat": 0, "lng": 0})
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "titulo": f"Mapa de {ciudad}",
            "lat": coordenadas["lat"],
            "lng": coordenadas["lng"]
        }
    )

# Endpoint API para obtener datos de equipos de La Liga
@app.get("/api/marcadores")
async def obtener_marcadores():
    return {
        "marcadores": [
            {"nombre": "Real Madrid CF", "ciudad": "Madrid", "estadio": "Santiago Bernabéu", "lat": 40.4530, "lng": -3.6883, "fundacion": 1902, "titulos_liga": 35},
            {"nombre": "FC Barcelona", "ciudad": "Barcelona", "estadio": "Spotify Camp Nou", "lat": 41.3809, "lng": 2.1228, "fundacion": 1899, "titulos_liga": 27},
            {"nombre": "Atlético de Madrid", "ciudad": "Madrid", "estadio": "Cívitas Metropolitano", "lat": 40.4361, "lng": -3.5994, "fundacion": 1903, "titulos_liga": 11},
            {"nombre": "Athletic Club", "ciudad": "Bilbao", "estadio": "San Mamés", "lat": 43.2641, "lng": -2.9501, "fundacion": 1898, "titulos_liga": 8},
            {"nombre": "Valencia CF", "ciudad": "Valencia", "estadio": "Mestalla", "lat": 39.4749, "lng": -0.3581, "fundacion": 1919, "titulos_liga": 6},
            {"nombre": "Real Sociedad", "ciudad": "San Sebastián", "estadio": "Reale Arena", "lat": 43.3014, "lng": -1.9738, "fundacion": 1909, "titulos_liga": 2},
            {"nombre": "Sevilla FC", "ciudad": "Sevilla", "estadio": "Ramón Sánchez-Pizjuán", "lat": 37.3841, "lng": -5.9704, "fundacion": 1890, "titulos_liga": 1},
            {"nombre": "Real Betis", "ciudad": "Sevilla", "estadio": "Benito Villamarín", "lat": 37.3565, "lng": -5.9826, "fundacion": 1907, "titulos_liga": 1},
            {"nombre": "RCD Mallorca", "ciudad": "Palma", "estadio": "Son Moix", "lat": 39.5905, "lng": 2.6296, "fundacion": 1916, "titulos_liga": 0},
            {"nombre": "Villarreal CF", "ciudad": "Villarreal", "estadio": "Estadio de la Cerámica", "lat": 39.9442, "lng": -0.1033, "fundacion": 1923, "titulos_liga": 0},
            {"nombre": "CA Osasuna", "ciudad": "Pamplona", "estadio": "El Sadar", "lat": 42.7960, "lng": -1.6370, "fundacion": 1920, "titulos_liga": 0},
            {"nombre": "Girona FC", "ciudad": "Girona", "estadio": "Montilivi", "lat": 41.9611, "lng": 2.8300, "fundacion": 1930, "titulos_liga": 0},
            {"nombre": "Celta de Vigo", "ciudad": "Vigo", "estadio": "Abanca Balaídos", "lat": 42.2117, "lng": -8.7396, "fundacion": 1923, "titulos_liga": 0},
            {"nombre": "UD Las Palmas", "ciudad": "Las Palmas", "estadio": "Gran Canaria", "lat": 28.1302, "lng": -15.4533, "fundacion": 1949, "titulos_liga": 0},
            {"nombre": "UD Almería", "ciudad": "Almería", "estadio": "Power Horse Stadium", "lat": 36.8344, "lng": -2.4089, "fundacion": 1989, "titulos_liga": 0},
            {"nombre": "Granada CF", "ciudad": "Granada", "estadio": "Nuevo Los Cármenes", "lat": 37.1526, "lng": -3.5952, "fundacion": 1931, "titulos_liga": 0},
            {"nombre": "Deportivo Alavés", "ciudad": "Vitoria", "estadio": "Mendizorroza", "lat": 42.8320, "lng": -2.6866, "fundacion": 1921, "titulos_liga": 0},
            {"nombre": "Rayo Vallecano", "ciudad": "Madrid", "estadio": "Vallecas", "lat": 40.3919, "lng": -3.6592, "fundacion": 1924, "titulos_liga": 0},
            {"nombre": "Cádiz CF", "ciudad": "Cádiz", "estadio": "Nuevo Mirandilla", "lat": 36.5019, "lng": -6.2709, "fundacion": 1910, "titulos_liga": 0},
            {"nombre": "CD Tenerife", "ciudad": "Santa Cruz de Tenerife", "estadio": "Heliodoro Rodríguez López", "lat": 28.4644, "lng": -16.2606, "fundacion": 1922, "titulos_liga": 0}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)