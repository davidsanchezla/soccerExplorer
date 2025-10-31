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

    // Inicializar el mapa centrado en Europa
    var map = L.map('map', {
        // Establecer límites de vista para Europa
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

// Función para crear un marcador
function createMarker(item) {
    const icon = L.divIcon({
        className: 'custom-div-icon',
        html: `<div style="background-color: ${ligaColors[item.liga] || '#000000'}; 
                         width: 10px; 
                         height: 10px; 
                         border-radius: 50%; 
                         border: 2px solid white;
                         box-shadow: 0 0 3px rgba(0,0,0,0.5);">
              </div>`,
        iconSize: [15, 15],
        iconAnchor: [7, 7]
    });

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
<<<<<<< HEAD
        // Limpiar marcadores existentes
        markersLayer.clearLayers();
        allMarkers = [];

        // Filtrar y mostrar solo los equipos de la liga seleccionada
        const marcadoresAMostrar = ligaFiltro 
            ? data.marcadores.filter(item => item.liga === ligaFiltro)
            : data.marcadores;

        // Crear y añadir los marcadores
        marcadoresAMostrar.forEach(item => {
            // Crear icono personalizado con el color de la liga
            const icon = L.divIcon({
                className: 'custom-div-icon',
                html: `<div style="background-color: ${ligaColors[item.liga] || '#000000'}; 
                                 width: 10px; 
                                 height: 10px; 
                                 border-radius: 50%; 
                                 border: 2px solid white;
                                 box-shadow: 0 0 3px rgba(0,0,0,0.5);">
                      </div>`,
                iconSize: [15, 15],
                iconAnchor: [7, 7]
            });
=======
        // Crear capas para cada liga
        const ligaLayers = {};
        
        data.marcadores.forEach(item => {
            let icon;
            
            // Si es un equipo de La Liga, usar el escudo
            if (item.liga === 'La Liga') {
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

                const nombreArchivo = equiposLaLiga[item.nombre];
                if (nombreArchivo) {
                    icon = L.icon({
                        iconUrl: `/static/img/escudos/laliga/${nombreArchivo}.png`,
                        iconSize: [40, 40],  // Tamaño del icono
                        iconAnchor: [20, 20], // Punto de anclaje
                        popupAnchor: [0, -20], // Punto del popup
                        className: 'team-icon'
                    });
                } else {
                    // Si no encuentra el nombre en el mapeo, usar círculo como respaldo
                    icon = L.divIcon({
                        className: 'custom-div-icon',
                        html: `<div style="background-color: ${ligaColors[item.liga]}; 
                                     width: 12px; 
                                     height: 12px; 
                                     border-radius: 50%; 
                                     border: 2px solid white;
                                     box-shadow: 0 0 4px rgba(0,0,0,0.5);">
                              </div>`,
                        iconSize: [16, 16],
                        iconAnchor: [8, 8]
                    });
                }
            } else {
                // Para el resto de ligas, usar el círculo de color
                icon = L.divIcon({
                    className: 'custom-div-icon',
                    html: `<div style="background-color: ${ligaColors[item.liga] || '#000000'}; 
                                    width: 10px; 
                                    height: 10px; 
                                    border-radius: 50%; 
                                    border: 2px solid white;
                                    box-shadow: 0 0 3px rgba(0,0,0,0.5);">
                            </div>`,
                    iconSize: [15, 15],
                    iconAnchor: [7, 7]
                });
            }
>>>>>>> 8e489711ae1120a3033421638cd7c3fc97e9f368

            var marker = L.marker([item.lat, item.lng], {icon: icon});
            
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
    });