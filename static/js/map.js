// Esperar a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
    // Definir colores por liga
    const ligaColors = {
        'La Liga': '#973949',           // Rojo
        'Premier League': '#3D195B',     // Morado
        'Serie A': '#008FD0',           // Azul
        'Bundesliga': '#6d1313',        // Rojo oscuro
        'Ligue 1': '#1c1faf'            // Azul marino
    };

    // Mapeo de equipos de La Liga con sus archivos de escudo
    const equiposLaLiga = {
        'Real Madrid': 'RealMadrid',
        'Barcelona': 'FCBarcelona',
        'Villarreal': 'Villareal',
        'Atletico Madrid': 'AtleticoDeMadrid',
        'Espanyol': 'Espanyol',
        'Real Betis': 'RealBetis',
        'Rayo Vallecano': 'RayoVallecano',
        'Elche': 'Elche',
        'Athletic Club': 'AthleticClub',
        'Getafe': 'Getafe',
        'Sevilla': 'Sevilla',
        'Alaves': 'Alaves',
        'Celta Vigo': 'Celta',
        'Osasuna': 'Osasuna',
        'Levante': 'Levante',
        'Mallorca': 'Mallorca',
        'Real Sociedad': 'RealSociedad',
        'Valencia': 'Valencia',
        'Real Oviedo': 'RealOviedo',
        'Girona': 'Girona'
    };

    // Inicializar el mapa centrado en Europa
    var map = L.map('map', {
        maxBounds: [
            [35.0, -15.0], // Esquina suroeste
            [65.0, 35.0]   // Esquina noreste
        ],
        minZoom: 4,
        maxZoom: 20,
        maxBoundsViscosity: 1.0,
        bounceAtZoomLimits: false
    }).setView([48, 10], 4); // Centro en Europa Central

    // Añadir capa de OpenStreetMap
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

    // Variables globales para los marcadores
    let allMarkers = [];
    let markersLayer = L.layerGroup().addTo(map);

    // Obtener el parámetro de liga de la URL
    const urlParams = new URLSearchParams(window.location.search);
    const ligaFiltro = urlParams.get('liga');

    // Función para centrar el mapa en los marcadores visibles
    function centerMapOnMarkers(markers) {
        if (markers.length > 0) {
            const bounds = L.latLngBounds(markers.map(marker => marker.getLatLng()));
            map.fitBounds(bounds, { padding: [50, 50] });
        }
    }

    // Función para crear un icono
    function createIcon(item) {
        if (item.liga === 'La Liga') {
            const nombreArchivo = equiposLaLiga[item.nombre];
            if (nombreArchivo) {
                return L.divIcon({
                    html: `<div class="team-icon" style="width: 36px; height: 36px; border-radius: 50%; background: white; padding: 2px; box-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                            <img src="/static/img/escudos/laliga/${nombreArchivo}.png" style="width: 100%; height: 100%; border-radius: 50%; object-fit: contain;">
                          </div>`,
                    iconSize: [40, 40],
                    iconAnchor: [20, 20],
                    popupAnchor: [0, -20],
                    className: 'team-marker'
                });
            }
        }
        
        // Para otros equipos o si no se encuentra el escudo
        return L.divIcon({
            className: 'custom-div-icon',
            html: `<div style="background-color: ${ligaColors[item.liga]}; 
                           width: ${item.liga === 'La Liga' ? '12' : '10'}px; 
                           height: ${item.liga === 'La Liga' ? '12' : '10'}px; 
                           border-radius: 50%; 
                           border: 2px solid white;
                           box-shadow: 0 0 ${item.liga === 'La Liga' ? '4' : '3'}px rgba(0,0,0,0.5);">
                  </div>`,
            iconSize: [item.liga === 'La Liga' ? 16 : 15, item.liga === 'La Liga' ? 16 : 15],
            iconAnchor: [item.liga === 'La Liga' ? 8 : 7, item.liga === 'La Liga' ? 8 : 7]
        });
    }

    // Función para crear un marcador
    function createMarker(item) {
        const icon = createIcon(item);
        const marker = L.marker([item.lat, item.lng], {icon: icon});
        
        marker.bindPopup(`
            <div style="border-left: 4px solid ${ligaColors[item.liga]}; padding-left: 10px;">
                <h3>${item.nombre}</h3>
                <p><strong>Liga:</strong> ${item.liga}</p>
                <p><strong>Estadio:</strong> ${item.estadio}</p>
                <p><strong>Ciudad:</strong> ${item.ciudad}</p>
            </div>
        `);
        
        marker.on('click', function(e) {
            document.getElementById('infoPanel').innerHTML = `
                <div style="border-left: 4px solid ${ligaColors[item.liga]}; padding-left: 10px;">
                    <h3>${item.nombre}</h3>
                    <p><strong>Liga:</strong> ${item.liga}</p>
                    <p><strong>Estadio:</strong> ${item.estadio}</p>
                    <p><strong>Ciudad:</strong> ${item.ciudad}</p>
                    <p><strong>Fundación:</strong> ${item.fundacion}</p>
                    <p><strong>Títulos de Liga:</strong> ${item.titulos_liga}</p>
                </div>
            `;
        });

        return marker;
    }

    // Obtener marcadores desde la API
    fetch('/api/marcadores')
        .then(response => response.json())
        .then(data => {
            console.log('Datos recibidos:', data);
            
            // Limpiar marcadores existentes
            markersLayer.clearLayers();
            allMarkers = [];

            // Filtrar y mostrar solo los equipos de la liga seleccionada
            const marcadoresAMostrar = ligaFiltro 
                ? data.marcadores.filter(item => item.liga === ligaFiltro)
                : data.marcadores;

            console.log('Marcadores a mostrar:', marcadoresAMostrar);

            // Crear y añadir los marcadores
            marcadoresAMostrar.forEach(item => {
                const marker = createMarker(item);
                allMarkers.push(marker);
                markersLayer.addLayer(marker);
            });

            // Centrar el mapa en los marcadores visibles
            centerMapOnMarkers(allMarkers);

            // Añadir título al mapa según la liga seleccionada
            if (ligaFiltro) {
                const mapTitle = document.createElement('div');
                mapTitle.className = 'map-title';
                mapTitle.innerHTML = `
                    <h2 style="
                        position: absolute;
                        top: 10px;
                        left: 50%;
                        transform: translateX(-50%);
                        background-color: white;
                        padding: 10px 20px;
                        border-radius: 5px;
                        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
                        z-index: 1000;
                        color: ${ligaColors[ligaFiltro]};
                        border-left: 4px solid ${ligaColors[ligaFiltro]};
                    ">${ligaFiltro}</h2>
                `;
                document.querySelector('#map').appendChild(mapTitle);
            }
        })
        .catch(error => {
            console.error('Error cargando los marcadores:', error);
            document.getElementById('infoPanel').innerHTML = `
                <div style="color: red; padding: 10px;">
                    <h3>Error al cargar los datos</h3>
                    <p>No se pudieron cargar los equipos. Por favor, intenta recargar la página.</p>
                </div>
            `;
        });
});