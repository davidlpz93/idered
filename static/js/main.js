// Variables
let boton_nav = document.querySelector('.nav-toggle');
let nav_menu = document.querySelector('.nav-menu');

// Eventos
boton_nav.addEventListener('click', function() {
    if(nav_menu.classList.contains('is-active')) {
        nav_menu.classList.remove('is-active');
    } else{
    nav_menu.classList.add('is-active');
    }
});