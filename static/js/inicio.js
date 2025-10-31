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
            const liga = button.textContent.trim();
            // Los botones de competiciones internacionales no tienen funcionalidad aún
            if (!['Champions League', 'Europa League', 'Conference League'].includes(liga)) {
                window.location.href = `/mapa?liga=${encodeURIComponent(liga)}`;
            }
        });
    });
});