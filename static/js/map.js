// Definir colores por liga
const ligaColors = {
    'La Liga': '#973949ff',           // Rojo
    'Premier League': '#3D195B',     // Morado
    'Serie A': '#008FD0',           // Azul
    'Bundesliga': '#6d1313ff',        // Rojo oscuro
    'Ligue 1': '#1c1fafff'            // Azul marino
};

// Inicializar el mapa centrado en Europa
var map = L.map('map', {
    // Establecer límites de vista para Europa
    maxBounds: [
        [25.0, -25.0], // Esquina suroeste
        [72.0, 55.0]   // Esquina noreste
    ],
    minZoom: 4,
    maxZoom: 20,
    maxBoundsViscosity: 1.0,
    bounceAtZoomLimits: false
}).setView([45, 10], 4); // Centro en Europa Central

// Añadir capa de OpenStreetMap
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Obtener marcadores desde la API
fetch('/api/marcadores')
    .then(response => response.json())
    .then(data => {
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

            // Añadir el marcador al mapa
            marker.addTo(map);
        });
    });