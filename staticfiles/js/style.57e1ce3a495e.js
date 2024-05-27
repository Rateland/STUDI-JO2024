document.addEventListener('DOMContentLoaded', function () {
    // Animation de survol du panier
    const panierLink = document.querySelector('.panier-link a');
    if (panierLink) {
        const primaryColor = getComputedStyle(document.documentElement).getPropertyValue('--primary-color').trim();

        panierLink.addEventListener('mouseenter', function () {
            panierLink.style.color = primaryColor; // Utiliser la couleur définie
        });
        panierLink.addEventListener('mouseleave', function () {
            panierLink.style.color = '';  // Restaure la couleur d'origine
        });
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            alert('Billet ajouté au panier !');
        });
    });
});

/* Pour le billet */
document.addEventListener('DOMContentLoaded', function () {
    const billetAction = document.querySelector('.billet-action');
    billetAction.addEventListener('click', function () {
        alert('Billet ajouté au panier !');
    });
});