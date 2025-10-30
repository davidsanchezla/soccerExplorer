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

# Endpoint API para obtener datos de equipos de las principales ligas europeas
@app.get("/api/marcadores")
async def obtener_marcadores():
    return {
        "marcadores": [
            # La Liga (España)
            {"nombre": "Real Madrid", "ciudad": "Madrid", "estadio": "Santiago Bernabéu", "lat": 40.4530, "lng": -3.6883, "fundacion": 1902, "titulos_liga": 35, "liga": "La Liga"},
            {"nombre": "Barcelona", "ciudad": "Barcelona", "estadio": "Spotify Camp Nou", "lat": 41.3809, "lng": 2.1228, "fundacion": 1899, "titulos_liga": 27, "liga": "La Liga"},
            {"nombre": "Villarreal", "ciudad": "Villarreal", "estadio": "Estadio de la Cerámica", "lat": 39.9442, "lng": -0.1033, "fundacion": 1923, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Atletico Madrid", "ciudad": "Madrid", "estadio": "Cívitas Metropolitano", "lat": 40.4361, "lng": -3.5994, "fundacion": 1903, "titulos_liga": 11, "liga": "La Liga"},
            {"nombre": "Espanyol", "ciudad": "Barcelona", "estadio": "RCDE Stadium", "lat": 41.3475, "lng": 2.0753, "fundacion": 1900, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Real Betis", "ciudad": "Sevilla", "estadio": "Benito Villamarín", "lat": 37.3565, "lng": -5.9826, "fundacion": 1907, "titulos_liga": 1, "liga": "La Liga"},
            {"nombre": "Rayo Vallecano", "ciudad": "Madrid", "estadio": "Vallecas", "lat": 40.3919, "lng": -3.6592, "fundacion": 1924, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Elche", "ciudad": "Elche", "estadio": "Martínez Valero", "lat": 38.2672, "lng": -0.6620, "fundacion": 1923, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Athletic Club", "ciudad": "Bilbao", "estadio": "San Mamés", "lat": 43.2641, "lng": -2.9501, "fundacion": 1898, "titulos_liga": 8, "liga": "La Liga"},
            {"nombre": "Getafe", "ciudad": "Getafe", "estadio": "Coliseum Alfonso Pérez", "lat": 40.3253, "lng": -3.7144, "fundacion": 1946, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Sevilla", "ciudad": "Sevilla", "estadio": "Ramón Sánchez-Pizjuán", "lat": 37.3841, "lng": -5.9704, "fundacion": 1890, "titulos_liga": 1, "liga": "La Liga"},
            {"nombre": "Alaves", "ciudad": "Vitoria", "estadio": "Mendizorroza", "lat": 42.8320, "lng": -2.6866, "fundacion": 1921, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Celta Vigo", "ciudad": "Vigo", "estadio": "Abanca Balaídos", "lat": 42.2117, "lng": -8.7396, "fundacion": 1923, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Osasuna", "ciudad": "Pamplona", "estadio": "El Sadar", "lat": 42.7960, "lng": -1.6370, "fundacion": 1920, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Levante", "ciudad": "Valencia", "estadio": "Ciutat de València", "lat": 39.4949, "lng": -0.3641, "fundacion": 1909, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Mallorca", "ciudad": "Palma", "estadio": "Son Moix", "lat": 39.5905, "lng": 2.6296, "fundacion": 1916, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Real Sociedad", "ciudad": "San Sebastián", "estadio": "Reale Arena", "lat": 43.3014, "lng": -1.9738, "fundacion": 1909, "titulos_liga": 2, "liga": "La Liga"},
            {"nombre": "Valencia", "ciudad": "Valencia", "estadio": "Mestalla", "lat": 39.4749, "lng": -0.3581, "fundacion": 1919, "titulos_liga": 6, "liga": "La Liga"},
            {"nombre": "Real Oviedo", "ciudad": "Oviedo", "estadio": "Carlos Tartiere", "lat": 43.3614, "lng": -5.8714, "fundacion": 1926, "titulos_liga": 0, "liga": "La Liga"},
            {"nombre": "Girona", "ciudad": "Girona", "estadio": "Montilivi", "lat": 41.9611, "lng": 2.8300, "fundacion": 1930, "titulos_liga": 0, "liga": "La Liga"},
            
            # Premier League (Inglaterra)
            {"nombre": "Manchester City", "ciudad": "Manchester", "estadio": "Etihad Stadium", "lat": 53.4831, "lng": -2.2004, "fundacion": 1880, "titulos_liga": 9, "liga": "Premier League"},
            
            # Serie A (Italia)
            {"nombre": "AC Milan", "ciudad": "Milán", "estadio": "San Siro", "lat": 45.4785, "lng": 9.1240, "fundacion": 1899, "titulos_liga": 19, "liga": "Serie A"},
            
            # Bundesliga (Alemania)
            {"nombre": "Bayern München", "ciudad": "Múnich", "estadio": "Allianz Arena", "lat": 48.2188, "lng": 11.6248, "fundacion": 1900, "titulos_liga": 33, "liga": "Bundesliga"},
            
            # Ligue 1 (Francia)
            {"nombre": "Paris Saint-Germain", "ciudad": "París", "estadio": "Parc des Princes", "lat": 48.8414, "lng": 2.2530, "fundacion": 1970, "titulos_liga": 11, "liga": "Ligue 1"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)