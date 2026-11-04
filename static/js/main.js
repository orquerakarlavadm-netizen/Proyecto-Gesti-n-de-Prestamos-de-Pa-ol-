document.addEventListener('DOMContentLoaded', () => {
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');

    navLinks.forEach((link) => {
        const href = link.getAttribute('href');
        if (!href) return;

        if (href === currentPath || (currentPath !== '/' && href.includes(currentPath))) {
            link.classList.add('active');
        }
    });

    const logoutForm = document.querySelector('.logout-form');
    if (logoutForm) {
        logoutForm.addEventListener('submit', (event) => {
            const confirmed = window.confirm('¿Deseas cerrar sesión?');
            if (!confirmed) {
                event.preventDefault();
            }
        });
    }

    console.log('Sistema Pañol - CTP Antonio Martín Marte iniciado correctamente.');
});