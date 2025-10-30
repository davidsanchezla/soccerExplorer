// Definir colores por liga
const ligaColors = {
    'La Liga': '#C8102E',           // Rojo
    'Premier League': '#3D195B',     // Morado
    'Serie A': '#008FD0',           // Azul
    'Bundesliga': '#DC052D',        // Rojo oscuro
    'Ligue 1': '#091C3E'            // Azul marino
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