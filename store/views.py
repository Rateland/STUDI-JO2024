from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from store.models import *
from django.db import transaction
from django.db.models import F
from django.contrib.auth.decorators import login_required

# Create your views here.
def accueil(request):
    epreuves = Epreuve.objects.all()
    billets = OffreBillet.objects.all()
    return render(request, 'store/accueil.html', context={"epreuves": epreuves, "billets": billets})

def epreuves_detail(request, slug):
    epreuve = get_object_or_404(Epreuve, slug=slug)
    offres = OffreBillet.objects.filter(epreuve=epreuve)  # Filtrer les offres par l'épreuve obtenue
    return render(request, 'store/epreuves.html', {'epreuve': epreuve, 'offres': offres})

def liste_epreuves(request):
    epreuves = Epreuve.objects.all()
    return render(request, 'store/liste_epreuves.html', {'epreuves': epreuves})


def billets_detail(request, slug):
    billet = get_object_or_404(OffreBillet, slug=slug)
    return render(request, 'store/billets.html', context={"billet": billet})


def ajout_panier(request, slug):
    billet = get_object_or_404(OffreBillet, slug=slug)
    
    # Créez ou récupérez le panier en session pour les utilisateurs non authentifiés
    if not request.user.is_authenticated:
        panier_id = request.session.get('panier_id')
        if panier_id:
            panier = Panier.objects.get(id=panier_id)
        else:
            panier = Panier.objects.create()
            request.session['panier_id'] = panier.id
    else:
        utilisateur = request.user
        panier, _ = Panier.objects.get_or_create(utilisateur=utilisateur)

    # Ajoutez le billet au panier
    achat, created = Achat.objects.get_or_create(billet=billet, defaults={'utilisateur': request.user if request.user.is_authenticated else None, 'quantité': 1})
    
    if not created:
        achat.quantité += 1
        achat.save()

    return redirect(billet.get_absolute_url())

@login_required
def acheter_billet(request, slug):
    # Démarre une transaction atomique
    with transaction.atomic():
        # Obtient l'objet billet et verrouille cette ligne dans la base de données jusqu'à la fin de la transaction
        billet = OffreBillet.objects.select_for_update().get(slug=slug)
        
        if billet.stock > 0:
            billet.stock = F('stock') - 1  # Utilise F pour éviter les conditions de course au niveau de la base de données
            billet.save(update_fields=['stock'])  # Met à jour seulement le champ 'stock'
            # Logique supplémentaire pour confirmer l'achat ou l'ajout au panier
            return redirect('confirmation_achat')  # Redirige vers une page de confirmation d'achat
        else:
            # Gère le cas où il n'y a plus de stock
            return HttpResponse("Désolé, il n'y a plus de billets disponibles.", status=400)