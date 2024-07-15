document.addEventListener('DOMContentLoaded', function () {
    console.log("Document fully loaded and parsed.");

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

    // Gestion du bouton "Ajouter au panier"
    const addToCartButtons = document.querySelectorAll('.add-to-cart');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            alert('Billet ajouté au panier !');
        });
    });

    // Gestion des actions de billet
    const billetAction = document.querySelector('.billet-action');
    if (billetAction) {
        billetAction.addEventListener('click', function () {
            alert('Billet ajouté au panier !');
        });
    }

    // Fonction de bascule pour les sections d'édition
    function toggleEdit(section) {
        console.log(`Toggling section: ${section}`);
        const displayDiv = document.getElementById(`${section}-display`);
        const form = document.getElementById(`${section}-form`);

        if (displayDiv.classList.contains('hidden')) {
            displayDiv.classList.remove('hidden');
            form.classList.add('hidden');
        } else {
            displayDiv.classList.add('hidden');
            form.classList.remove('hidden');
        }
    }

    // Assurez-vous que la fonction est globale pour qu'elle puisse être appelée depuis le HTML
    window.toggleEdit = toggleEdit;
});
