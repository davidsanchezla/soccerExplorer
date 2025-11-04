document.addEventListener('DOMContentLoaded', function() {
    // Funcionalidad del menú hamburguesa
    const menuToggle = document.getElementById('menuToggle');
    const sideMenu = document.getElementById('sideMenu');
    
    menuToggle.addEventListener('click', function() {
        sideMenu.classList.toggle('active');
    });

    // Funcionalidad del pin del mapa
    const mapPin = document.getElementById('mapPin');
    mapPin.addEventListener('click', function() {
        window.location.href = '/mapa';
    });

    // Funcionalidad de los botones de ligas
    const leagueButtons = document.querySelectorAll('.league-button');
    
    leagueButtons.forEach(button => {
        button.addEventListener('click', function() {
            const liga = button.dataset.league || button.querySelector('.league-name').textContent.trim();
            // Manejar ligas nacionales e internacionales
            if (liga === 'Champions League') {
                window.location.href = `/mapa?liga=${encodeURIComponent(liga)}`;
            } else if (!button.classList.contains('international')) {
                window.location.href = `/mapa?liga=${encodeURIComponent(liga)}`;
            }
        });

        // Añadir efecto de sonido al hover (opcional)
        button.addEventListener('mouseenter', function() {
            if (button.classList.contains('playing')) return;
            button.classList.add('playing');
            setTimeout(() => button.classList.remove('playing'), 300);
        });
    });

    // Importar countryMetadata de map.js si está disponible globalmente
    // Si no, copiar el objeto countryMetadata aquí
    const countryMetadata = {
        'ESP': { colors: ['#FF0000', '#FFFF00', '#FF0000'], alignment: 'horizontal' },
        'FRA': { colors: ['#0000FF', '#FFFFFF', '#FF0000'], alignment: 'vertical' },
        'ENG': { colors: ['#FFFFFF', '#FF0000'], alignment: 'vertical' },
        'GER': { colors: ['#000000', '#FF0000', '#FFFF00'], alignment: 'horizontal' },
        'ITA': { colors: ['#008000', '#FFFFFF', '#FF0000'], alignment: 'horizontal' }
        // Añadir más países según sea necesario
    };

    function applyCountryStyles(countryCode, element) {
        const metadata = countryMetadata[countryCode];
        if (metadata) {
            const { colors, alignment } = metadata;
            const gradient = alignment === 'horizontal'
                ? `linear-gradient(to right, ${colors.join(', ')})`
                : `linear-gradient(to bottom, ${colors.join(', ')})`;
            element.style.background = gradient;
        }
    }

    // Nota: No asignamos fondo fijo a las ligas nacionales para que
    // el color sólo aparezca en hover vía CSS (como en los internacionales).
    // Las reglas en inicio.css gestionan background, border y shadow al hover.
});