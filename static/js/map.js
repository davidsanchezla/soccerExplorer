// Inicializar el mapa centrado en Europa
var map = L.map('map').setView([40.4168, -3.7038], 4);

// Añadir capa de OpenStreetMap
L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '© <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

// Obtener marcadores desde la API
fetch('/api/marcadores')
    .then(response => response.json())
    .then(data => {
        data.marcadores.forEach(item => {
            var marker = L.marker([item.lat, item.lng]).addTo(map);
            
            marker.bindPopup(`
                <b>${item.nombre}</b>
                <p><strong>Estadio:</strong> ${item.estadio}</p>
                <p><strong>Ciudad:</strong> ${item.ciudad}</p>
            `);
            
            marker.on('click', function(e) {
                document.getElementById('infoPanel').innerHTML = `
                    <h3>${item.nombre}</h3>
                    <p><strong>Estadio:</strong> ${item.estadio}</p>
                    <p><strong>Ciudad:</strong> ${item.ciudad}</p>
                    <p><strong>Fundación:</strong> ${item.fundacion}</p>
                    <p><strong>Títulos de Liga:</strong> ${item.titulos_liga}</p>
                `;
            });
        });
    });