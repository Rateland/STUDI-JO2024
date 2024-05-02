document.addEventListener('DOMContentLoaded', function () {
    // Animation de survol du panier
    const panierLink = document.querySelector('.panier-link a');
    if (panierLink) {
        panierLink.addEventListener('mouseenter', function () {
            panierLink.style.color = 'red';  // Change la couleur lors du survol
        });
        panierLink.addEventListener('mouseleave', function () {
            panierLink.style.color = '';  // Restaure la couleur d'origine
        });
    }
});
