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
            // Los botones de competiciones internacionales no tienen funcionalidad aún
            if (!button.classList.contains('international')) {
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
});