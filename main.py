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

# Ruta principal que sirve la página de inicio
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="inicio.html",
        context={"titulo": "Soccer Explorer - Inicio"}
    )

# Ruta para el mapa interactivo
@app.get("/mapa", response_class=HTMLResponse)
async def mapa(request: Request, liga: str = None):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "titulo": "Mapa Mundial Interactivo",
            "liga_filtro": liga
        }
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
            
            # Ligue 1 (Francia)
            {"nombre": "Paris Saint-Germain", "ciudad": "París", "estadio": "Parc des Princes", "lat": 48.8414, "lng": 2.2530, "fundacion": 1970, "titulos_liga": 11, "liga": "Ligue 1"},
            {"nombre": "Angers", "ciudad": "Angers", "estadio": "Stade Raymond Kopa", "lat": 47.4622, "lng": -0.5253, "fundacion": 1919, "titulos_liga": 0, "liga": "Ligue 1"},
            {"nombre": "Auxerre", "ciudad": "Auxerre", "estadio": "Stade de l'Abbé-Deschamps", "lat": 47.7833, "lng": 3.5833, "fundacion": 1905, "titulos_liga": 1, "liga": "Ligue 1"},
            {"nombre": "Brest", "ciudad": "Brest", "estadio": "Stade Francis-Le Blé", "lat": 48.4028, "lng": -4.4436, "fundacion": 1950, "titulos_liga": 0, "liga": "Ligue 1"},
            {"nombre": "Estrasburgo", "ciudad": "Estrasburgo", "estadio": "Stade de la Meinau", "lat": 48.5734, "lng": 7.7521, "fundacion": 1906, "titulos_liga": 1, "liga": "Ligue 1"},
            {"nombre": "Le Havre", "ciudad": "Le Havre", "estadio": "Stade Océane", "lat": 49.4944, "lng": 0.1470, "fundacion": 1872, "titulos_liga": 0, "liga": "Ligue 1"},
            {"nombre": "Lens", "ciudad": "Lens", "estadio": "Stade Bollaert-Delelis", "lat": 50.4328, "lng": 2.8154, "fundacion": 1906, "titulos_liga": 1, "liga": "Ligue 1"},
            {"nombre": "Lille", "ciudad": "Lille", "estadio": "Stade Pierre-Mauroy", "lat": 50.6119, "lng": 3.1307, "fundacion": 1944, "titulos_liga": 4, "liga": "Ligue 1"},
            {"nombre": "Lorient", "ciudad": "Lorient", "estadio": "Stade du Moustoir", "lat": 47.7486, "lng": -3.3704, "fundacion": 1926, "titulos_liga": 0, "liga": "Ligue 1"},
            {"nombre": "Lyon", "ciudad": "Lyon", "estadio": "Groupama Stadium", "lat": 45.7653, "lng": 4.9822, "fundacion": 1950, "titulos_liga": 7, "liga": "Ligue 1"},
            {"nombre": "Marsella", "ciudad": "Marsella", "estadio": "Stade Vélodrome", "lat": 43.2696, "lng": 5.3956, "fundacion": 1899, "titulos_liga": 9, "liga": "Ligue 1"},
            {"nombre": "Metz", "ciudad": "Metz", "estadio": "Stade Saint-Symphorien", "lat": 49.1097, "lng": 6.1742, "fundacion": 1932, "titulos_liga": 0, "liga": "Ligue 1"},
            {"nombre": "Mónaco", "ciudad": "Mónaco", "estadio": "Stade Louis II", "lat": 43.7277, "lng": 7.4167, "fundacion": 1924, "titulos_liga": 8, "liga": "Ligue 1"},
            {"nombre": "Nantes", "ciudad": "Nantes", "estadio": "Stade de la Beaujoire", "lat": 47.2559, "lng": -1.5250, "fundacion": 1943, "titulos_liga": 8, "liga": "Ligue 1"},
            {"nombre": "Niza", "ciudad": "Niza", "estadio": "Allianz Riviera", "lat": 43.7034, "lng": 7.2663, "fundacion": 1904, "titulos_liga": 4, "liga": "Ligue 1"},
            {"nombre": "Paris FC", "ciudad": "París", "estadio": "Stade Charléty", "lat": 48.8184, "lng": 2.3457, "fundacion": 1969, "titulos_liga": 0, "liga": "Ligue 1"},
            {"nombre": "Rennes", "ciudad": "Rennes", "estadio": "Roazhon Park", "lat": 48.1078, "lng": -1.7124, "fundacion": 1901, "titulos_liga": 0, "liga": "Ligue 1"},
            {"nombre": "Toulouse", "ciudad": "Toulouse", "estadio": "Stadium de Toulouse", "lat": 43.5828, "lng": 1.4375, "fundacion": 1937, "titulos_liga": 0, "liga": "Ligue 1"},

            # Premier League (Inglaterra)
            {"nombre": "Arsenal", "ciudad": "Londres", "estadio": "Emirates Stadium", "lat": 51.5549, "lng": -0.1084, "fundacion": 1886, "titulos_liga": 13, "liga": "Premier League"},
            {"nombre": "Aston Villa", "ciudad": "Birmingham", "estadio": "Villa Park", "lat": 52.5090, "lng": -1.8850, "fundacion": 1874, "titulos_liga": 7, "liga": "Premier League"},
            {"nombre": "Bournemouth", "ciudad": "Bournemouth", "estadio": "Vitality Stadium", "lat": 50.7352, "lng": -1.8384, "fundacion": 1899, "titulos_liga": 0, "liga": "Premier League"},
            {"nombre": "Brentford", "ciudad": "Londres", "estadio": "Gtech Community Stadium", "lat": 51.4881, "lng": -0.3025, "fundacion": 1889, "titulos_liga": 0, "liga": "Premier League"},
            {"nombre": "Brighton", "ciudad": "Brighton", "estadio": "Amex Stadium", "lat": 50.8614, "lng": -0.0834, "fundacion": 1901, "titulos_liga": 0, "liga": "Premier League"},
            {"nombre": "Burnley", "ciudad": "Burnley", "estadio": "Turf Moor", "lat": 53.7890, "lng": -2.2303, "fundacion": 1882, "titulos_liga": 2, "liga": "Premier League"},
            {"nombre": "Chelsea", "ciudad": "Londres", "estadio": "Stamford Bridge", "lat": 51.4817, "lng": -0.1910, "fundacion": 1905, "titulos_liga": 6, "liga": "Premier League"},
            {"nombre": "Crystal Palace", "ciudad": "Londres", "estadio": "Selhurst Park", "lat": 51.3983, "lng": -0.0866, "fundacion": 1905, "titulos_liga": 0, "liga": "Premier League"},
            {"nombre": "Everton", "ciudad": "Liverpool", "estadio": "Goodison Park", "lat": 53.4389, "lng": -2.9664, "fundacion": 1878, "titulos_liga": 9, "liga": "Premier League"},
            {"nombre": "Fulham", "ciudad": "Londres", "estadio": "Craven Cottage", "lat": 51.4749, "lng": -0.2216, "fundacion": 1879, "titulos_liga": 0, "liga": "Premier League"},
            {"nombre": "Leeds United", "ciudad": "Leeds", "estadio": "Elland Road", "lat": 53.7778, "lng": -1.5724, "fundacion": 1919, "titulos_liga": 3, "liga": "Premier League"},
            {"nombre": "Liverpool", "ciudad": "Liverpool", "estadio": "Anfield", "lat": 53.4308, "lng": -2.9608, "fundacion": 1892, "titulos_liga": 19, "liga": "Premier League"},
            {"nombre": "Manchester City", "ciudad": "Manchester", "estadio": "Etihad Stadium", "lat": 53.4831, "lng": -2.2004, "fundacion": 1880, "titulos_liga": 9, "liga": "Premier League"},
            {"nombre": "Manchester United", "ciudad": "Manchester", "estadio": "Old Trafford", "lat": 53.4631, "lng": -2.2913, "fundacion": 1878, "titulos_liga": 20, "liga": "Premier League"},
            {"nombre": "Newcastle United", "ciudad": "Newcastle", "estadio": "St James' Park", "lat": 54.9756, "lng": -1.6217, "fundacion": 1892, "titulos_liga": 4, "liga": "Premier League"},
            {"nombre": "Nottingham Forest", "ciudad": "Nottingham", "estadio": "City Ground", "lat": 52.9401, "lng": -1.1326, "fundacion": 1865, "titulos_liga": 1, "liga": "Premier League"},
            {"nombre": "Sunderland", "ciudad": "Sunderland", "estadio": "Stadium of Light", "lat": 54.9146, "lng": -1.3882, "fundacion": 1879, "titulos_liga": 6, "liga": "Premier League"},
            {"nombre": "Tottenham Hotspur", "ciudad": "Londres", "estadio": "Tottenham Hotspur Stadium", "lat": 51.6033, "lng": -0.0658, "fundacion": 1882, "titulos_liga": 2, "liga": "Premier League"},
            {"nombre": "West Ham United", "ciudad": "Londres", "estadio": "London Stadium", "lat": 51.5387, "lng": -0.0166, "fundacion": 1895, "titulos_liga": 0, "liga": "Premier League"},
            {"nombre": "Wolverhampton", "ciudad": "Wolverhampton", "estadio": "Molineux Stadium", "lat": 52.5908, "lng": -2.1308, "fundacion": 1877, "titulos_liga": 3, "liga": "Premier League"},

            # Serie A (Italia)
            {"nombre": "Atalanta", "ciudad": "Bérgamo", "estadio": "Gewiss Stadium", "lat": 45.7089, "lng": 9.6866, "fundacion": 1907, "titulos_liga": 0, "liga": "Serie A"},
            {"nombre": "Bologna", "ciudad": "Bolonia", "estadio": "Stadio Renato Dall'Ara", "lat": 44.4922, "lng": 11.3093, "fundacion": 1909, "titulos_liga": 7, "liga": "Serie A"},
            {"nombre": "Cagliari", "ciudad": "Cagliari", "estadio": "Unipol Domus", "lat": 39.1989, "lng": 9.1328, "fundacion": 1920, "titulos_liga": 1, "liga": "Serie A"},
            {"nombre": "Como", "ciudad": "Como", "estadio": "Stadio Giuseppe Sinigaglia", "lat": 45.8114, "lng": 9.0827, "fundacion": 1907, "titulos_liga": 0, "liga": "Serie A"},
            {"nombre": "Cremonese", "ciudad": "Cremona", "estadio": "Stadio Giovanni Zini", "lat": 45.1367, "lng": 10.0289, "fundacion": 1903, "titulos_liga": 0, "liga": "Serie A"},
            {"nombre": "Fiorentina", "ciudad": "Florencia", "estadio": "Stadio Artemio Franchi", "lat": 43.7808, "lng": 11.2826, "fundacion": 1926, "titulos_liga": 2, "liga": "Serie A"},
            {"nombre": "Genoa", "ciudad": "Génova", "estadio": "Stadio Luigi Ferraris", "lat": 44.4166, "lng": 8.9528, "fundacion": 1893, "titulos_liga": 9, "liga": "Serie A"},
            {"nombre": "Inter", "ciudad": "Milán", "estadio": "San Siro", "lat": 45.4781, "lng": 9.1240, "fundacion": 1908, "titulos_liga": 19, "liga": "Serie A"},
            {"nombre": "Juventus", "ciudad": "Turín", "estadio": "Allianz Stadium", "lat": 45.1096, "lng": 7.6413, "fundacion": 1897, "titulos_liga": 36, "liga": "Serie A"},
            {"nombre": "Lazio", "ciudad": "Roma", "estadio": "Stadio Olimpico", "lat": 41.9341, "lng": 12.4547, "fundacion": 1900, "titulos_liga": 2, "liga": "Serie A"},
            {"nombre": "Lecce", "ciudad": "Lecce", "estadio": "Stadio Via del Mare", "lat": 40.3568, "lng": 18.1825, "fundacion": 1908, "titulos_liga": 0, "liga": "Serie A"},
            {"nombre": "Milan", "ciudad": "Milán", "estadio": "San Siro", "lat": 45.4785, "lng": 9.1240, "fundacion": 1899, "titulos_liga": 19, "liga": "Serie A"},
            {"nombre": "Napoli", "ciudad": "Nápoles", "estadio": "Stadio Diego Armando Maradona", "lat": 40.8279, "lng": 14.1931, "fundacion": 1926, "titulos_liga": 3, "liga": "Serie A"},
            {"nombre": "Parma", "ciudad": "Parma", "estadio": "Stadio Ennio Tardini", "lat": 44.7947, "lng": 10.3385, "fundacion": 1913, "titulos_liga": 0, "liga": "Serie A"},
            {"nombre": "Pisa", "ciudad": "Pisa", "estadio": "Arena Garibaldi", "lat": 43.7228, "lng": 10.3928, "fundacion": 1909, "titulos_liga": 0, "liga": "Serie A"},
            {"nombre": "Roma", "ciudad": "Roma", "estadio": "Stadio Olimpico", "lat": 41.9341, "lng": 12.4547, "fundacion": 1927, "titulos_liga": 3, "liga": "Serie A"},
            {"nombre": "Sassuolo", "ciudad": "Sassuolo", "estadio": "Mapei Stadium", "lat": 44.7156, "lng": 10.6492, "fundacion": 1920, "titulos_liga": 0, "liga": "Serie A"},
            {"nombre": "Torino", "ciudad": "Turín", "estadio": "Stadio Olimpico Grande Torino", "lat": 45.0419, "lng": 7.6501, "fundacion": 1906, "titulos_liga": 7, "liga": "Serie A"},
            {"nombre": "Udinese", "ciudad": "Udine", "estadio": "Dacia Arena", "lat": 46.0819, "lng": 13.2001, "fundacion": 1896, "titulos_liga": 0, "liga": "Serie A"},
            {"nombre": "Hellas Verona", "ciudad": "Verona", "estadio": "Stadio Marcantonio Bentegodi", "lat": 45.4350, "lng": 10.9683, "fundacion": 1903, "titulos_liga": 1, "liga": "Serie A"},

            # Bundesliga (Alemania)
            {"nombre": "Augsburg", "ciudad": "Augsburgo", "estadio": "WWK Arena", "lat": 48.3249, "lng": 10.8852, "fundacion": 1907, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "Bayer Leverkusen", "ciudad": "Leverkusen", "estadio": "BayArena", "lat": 51.0383, "lng": 7.0022, "fundacion": 1904, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "Bayern München", "ciudad": "Múnich", "estadio": "Allianz Arena", "lat": 48.2188, "lng": 11.6248, "fundacion": 1900, "titulos_liga": 33, "liga": "Bundesliga"},
            {"nombre": "Borussia Dortmund", "ciudad": "Dortmund", "estadio": "Signal Iduna Park", "lat": 51.4926, "lng": 7.4517, "fundacion": 1909, "titulos_liga": 8, "liga": "Bundesliga"},
            {"nombre": "Borussia Mönchengladbach", "ciudad": "Mönchengladbach", "estadio": "Borussia-Park", "lat": 51.1745, "lng": 6.3857, "fundacion": 1900, "titulos_liga": 5, "liga": "Bundesliga"},
            {"nombre": "Köln", "ciudad": "Colonia", "estadio": "RheinEnergieStadion", "lat": 50.9335, "lng": 6.8750, "fundacion": 1948, "titulos_liga": 3, "liga": "Bundesliga"},
            {"nombre": "Eintracht Frankfurt", "ciudad": "Fráncfort", "estadio": "Deutsche Bank Park", "lat": 50.0687, "lng": 8.6450, "fundacion": 1899, "titulos_liga": 1, "liga": "Bundesliga"},
            {"nombre": "Freiburg", "ciudad": "Friburgo", "estadio": "Europa-Park Stadion", "lat": 47.9990, "lng": 7.8930, "fundacion": 1904, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "Hamburger SV", "ciudad": "Hamburgo", "estadio": "Volksparkstadion", "lat": 53.5871, "lng": 9.8987, "fundacion": 1887, "titulos_liga": 6, "liga": "Bundesliga"},
            {"nombre": "Heidenheim", "ciudad": "Heidenheim", "estadio": "Voith-Arena", "lat": 48.6760, "lng": 10.1570, "fundacion": 1846, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "Hoffenheim", "ciudad": "Sinsheim", "estadio": "PreZero Arena", "lat": 49.2394, "lng": 8.8935, "fundacion": 1899, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "Mainz 05", "ciudad": "Maguncia", "estadio": "MEWA Arena", "lat": 49.9847, "lng": 8.2244, "fundacion": 1905, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "RB Leipzig", "ciudad": "Leipzig", "estadio": "Red Bull Arena", "lat": 51.3456, "lng": 12.3480, "fundacion": 2009, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "St. Pauli", "ciudad": "Hamburgo", "estadio": "Millerntor-Stadion", "lat": 53.5549, "lng": 9.9670, "fundacion": 1910, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "Stuttgart", "ciudad": "Stuttgart", "estadio": "Mercedes-Benz Arena", "lat": 48.7925, "lng": 9.2320, "fundacion": 1893, "titulos_liga": 5, "liga": "Bundesliga"},
            {"nombre": "Union Berlin", "ciudad": "Berlín", "estadio": "Stadion An der Alten Försterei", "lat": 52.4583, "lng": 13.5683, "fundacion": 1966, "titulos_liga": 0, "liga": "Bundesliga"},
            {"nombre": "Werder Bremen", "ciudad": "Bremen", "estadio": "Weserstadion", "lat": 53.0667, "lng": 8.8407, "fundacion": 1899, "titulos_liga": 4, "liga": "Bundesliga"},
            {"nombre": "Wolfsburg", "ciudad": "Wolfsburgo", "estadio": "Volkswagen Arena", "lat": 52.4321, "lng": 10.8034, "fundacion": 1945, "titulos_liga": 1, "liga": "Bundesliga"}
        ]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)