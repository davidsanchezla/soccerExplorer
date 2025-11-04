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

    // Aplicar color de liga a los botones de liga nacional
    leagueButtons.forEach(button => {
        const liga = button.dataset.league;
        if (liga && !button.classList.contains('international')) {
            // Usar color de liga
            const ligaColors = {
                'La Liga': '#973949',
                'Premier League': '#3D195B',
                'Serie A': '#008FD0',
                'Bundesliga': '#6d1313',
                'Ligue 1': '#1c1faf'
            };
            button.style.background = ligaColors[liga] || '#ccc';
        }
    });
});