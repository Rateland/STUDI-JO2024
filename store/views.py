from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from store.models import *
from django.db import transaction
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def accueil(request):
    epreuves = Epreuve.objects.all()
    billets = OffreBillet.objects.all()
    return render(request, 'store/accueil.html', context={"epreuves": epreuves, "billets": billets})

def epreuves_detail(request, slug):
    epreuve = get_object_or_404(Epreuve, slug=slug)
    offres = OffreBillet.objects.all()  # Si vous souhaitez afficher tous les types d'offres disponibles
    return render(request, 'store/epreuves.html', {'epreuve': epreuve, 'offres': offres})

def liste_epreuves(request):
    epreuves = Epreuve.objects.all()
    return render(request, 'store/liste_epreuves.html', {'epreuves': epreuves})


def billets_detail(request, slug):
    billet = get_object_or_404(OffreBillet, slug=slug)
    return render(request, 'store/billets.html', context={"billet": billet})

def ajout_panier(request, epreuve_slug, billet_slug):
    # Récupérer l'épreuve et l'offre de billet par leurs slugs
    epreuve = get_object_or_404(Epreuve, slug=epreuve_slug)
    billet = get_object_or_404(OffreBillet, slug=billet_slug)
    
    if request.user.is_authenticated:
        # Récupérer ou créer le panier pour l'utilisateur connecté
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
        # Récupérer ou créer l'achat associé au panier et à l'utilisateur
        achat, created = Achat.objects.get_or_create(
            billet=billet,
            utilisateur=request.user,
            defaults={'quantité': 1, 'epreuve': epreuve}
        )
        if not created:
            # Si l'achat existe déjà, augmenter la quantité
            achat.quantité += 1
            achat.save()
    else:
        # Gérer le panier temporaire pour les utilisateurs non authentifiés
        panier_temp = request.session.get('panier_temp', [])
        for item in panier_temp:
            if item['billet_id'] == billet.id:
                # Si le billet existe déjà dans le panier temporaire, augmenter la quantité
                item['quantité'] += 1
                break
        else:
            # Sinon, ajouter un nouvel article au panier temporaire
            panier_temp.append({'billet_id': billet.id, 'quantité': 1, 'epreuve_id': epreuve.id})
        # Sauvegarder le panier temporaire dans la session
        request.session['panier_temp'] = panier_temp

    # Redirection vers la vue du panier
    return redirect('voir_panier')

def voir_panier(request):
    if not request.user.is_authenticated:
        # Redirection vers la page de connexion si l'utilisateur n'est pas authentifié
        login_url = reverse('login')
        return redirect(f"{login_url}?next={request.path}")

    # Récupérer ou créer le panier pour l'utilisateur connecté
    panier, _ = Panier.objects.get_or_create(utilisateur=request.user)

    # Si un panier temporaire existe dans la session
    if 'panier_temp' in request.session:
        panier_temp = request.session.pop('panier_temp')
        for item in panier_temp:
            # Récupérer le billet associé à l'ID stocké dans le panier temporaire
            billet = OffreBillet.objects.get(id=item['billet_id'])
            # Récupérer ou créer l'achat pour l'utilisateur authentifié
            achat, created = Achat.objects.get_or_create(
                billet=billet,
                utilisateur=request.user,
                defaults={'quantité': item['quantité'], 'epreuve_id': item['epreuve_id']}
            )
            if not created:
                # Si l'achat existe déjà, augmenter la quantité
                achat.quantité += item['quantité']
                achat.save()
    
    # Calculer le total du panier en fonction de la quantité et du prix de chaque billet
    total = sum(achat.quantité * achat.billet.prix for achat in panier.achats.all())
    # Rendre le modèle du panier avec les détails
    return render(request, 'store/panier.html', {'panier': panier, 'total': total})

@login_required     
def procéder_au_paiement(request):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        panier = Panier.objects.get(utilisateur=request.user)
        if panier.achats.exists():
            # Ici, intégrez la logique de paiement
            # Après le paiement réussi :
            panier.acheté = True
            panier.save()
            return render(request, 'store/confirmation_paiement.html')
        else:
            return redirect('voir_panier')
    except Panier.DoesNotExist:
        return redirect('voir_panier')