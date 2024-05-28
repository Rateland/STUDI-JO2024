from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.db.models import F, Sum
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.urls import reverse
from store.models import *
from store.QRcode import *

# Create your views here.
def accueil(request):
    epreuves = Epreuve.objects.all()
    billets = OffreBillet.objects.all()

    if request.user.is_authenticated:
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
        panier_total = Achat.objects.filter(panier=panier).aggregate(Sum('quantité'))['quantité__sum'] or 0
    else:
        panier_total = 0

    return render(request, 'store/accueil.html', context={"epreuves": epreuves, "billets": billets, "panier_total": panier_total})

def mentions_legales(request):
    return render(request, 'mentions_legales.html')

def epreuves_detail(request, slug):
    epreuve = get_object_or_404(Epreuve, slug=slug)
    offres = OffreBillet.objects.all()  # Si vous souhaitez afficher tous les types d'offres disponibles
    
    
    panier_total = 0
    if request.user.is_authenticated:
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
        panier_total = Achat.objects.filter(panier=panier).aggregate(Sum('quantité'))['quantité__sum'] or 0

    return render(request, 'store/epreuves.html', {'epreuve': epreuve, 'offres': offres, 'panier_total': panier_total})

def liste_epreuves(request):
    epreuves = Epreuve.objects.all()

    panier_total = 0
    if request.user.is_authenticated:
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
        panier_total = Achat.objects.filter(panier=panier).aggregate(Sum('quantité'))['quantité__sum'] or 0

    return render(request, 'store/liste_epreuves.html', {'epreuves': epreuves, 'panier_total': panier_total})

def billets_detail(request, slug):
    billet = get_object_or_404(OffreBillet, slug=slug)

    panier_total = 0
    if request.user.is_authenticated:
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
        panier_total = Achat.objects.filter(panier=panier).aggregate(Sum('quantité'))['quantité__sum'] or 0

    return render(request, 'store/billets.html', context={"billet": billet})

def liste_billets(request):
    billets = OffreBillet.objects.all

    panier_total = 0
    if request.user.is_authenticated:
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
        panier_total = Achat.objects.filter(panier=panier).aggregate(Sum('quantité'))['quantité__sum'] or 0

    return render(request, 'store/liste_offres.html', {'billets': billets, 'panier_total': panier_total})

def ajout_panier(request, epreuve_slug, billet_slug):
    epreuve = get_object_or_404(Epreuve, slug=epreuve_slug)
    billet = get_object_or_404(OffreBillet, slug=billet_slug)
    
    if request.user.is_authenticated:
        panier, created = Panier.objects.get_or_create(utilisateur=request.user)
        achat, created = Achat.objects.get_or_create(
            billet=billet,
            utilisateur=request.user,
            defaults={'quantité': 1, 'epreuve': epreuve, 'panier': panier}  # Associez le panier ici
        )
        if not created:
            achat.quantité += 1
            achat.save()
    else:
        panier_temp = request.session.get('panier_temp', [])
        for item in panier_temp:
            if item['billet_id'] == billet.id:
                item['quantité'] += 1
                break
        else:
            panier_temp.append({'billet_id': billet.id, 'quantité': 1, 'epreuve_id': epreuve.id})
        request.session['panier_temp'] = panier_temp

    return redirect(request.META.get('HTTP_REFERER', 'accueil'))

def voir_panier(request):
    if not request.user.is_authenticated:
        messages.info(request, "Vous devez être connecté pour accéder au panier.")
        login_url = reverse('login')
        return redirect(f"{login_url}?next={request.path}")

    panier, _ = Panier.objects.get_or_create(utilisateur=request.user)

    if 'panier_temp' in request.session:
        panier_temp = request.session.pop('panier_temp')
        for item in panier_temp:
            billet = OffreBillet.objects.get(id=item['billet_id'])
            achat, created = Achat.objects.get_or_create(
                billet=billet,
                utilisateur=request.user,
                defaults={'quantité': item['quantité'], 'epreuve_id': item['epreuve_id']}
            )
            if not created:
                achat.quantité += item['quantité']
                achat.save()
            achat.panier = panier
            achat.save()

    total = 0
    achats = Achat.objects.filter(panier=panier)
    for achat in achats:
        montant_total = achat.quantité * achat.billet.prix
        achat.montant_total = montant_total
        total += montant_total

    panier_total = achats.aggregate(Sum('quantité'))['quantité__sum'] or 0

    return render(request, 'store/panier.html', {'panier': panier, 'total': total, 'achats': achats, 'panier_total': panier_total})

def supprimer_achat(request, achat_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    try:
        achat = Achat.objects.get(id=achat_id, utilisateur=request.user)
        achat.delete()
    except Achat.DoesNotExist:
        messages.error(request, "Cet achat n'existe pas ou n'est pas dans votre panier.")
    
    return redirect('voir_panier')

@login_required
def paiement(request):
    utilisateur = request.user
    try:
        panier = Panier.objects.get(utilisateur=utilisateur)
        achats = Achat.objects.filter(panier=panier)
        if achats.exists():
            total = sum(achat.quantité * achat.billet.prix for achat in achats)

            # Simuler le paiement
            transaction_id, status = simulate_payment(total)

            try:
                # Créer une nouvelle transaction
                transaction = Transaction.objects.create(
                    utilisateur=utilisateur,
                    panier=panier,
                    montant_total=total,
                    status=status,
                    date_transaction=timezone.now()
                )

                # Créer le ticket associé à la transaction
                ticket = Ticket.objects.create(
                    transaction=transaction,
                    utilisateur=utilisateur,
                    montant_total=total
                )
                ticket.achats.set(achats)
                ticket.save()

                # Générer le code QR
                generate_qr_code(ticket)

                panier.acheté = True
                panier.date_achat = timezone.now()
                panier.save()

                # Vider le panier
                achats.delete()

                messages.success(request, "Paiement réussi. Merci pour votre achat !")
                send_confirmation_email(ticket)
                return render(request, 'store/confirmation_paiement.html', {'ticket': ticket})
            except Exception as e:
                messages.error(request, f"Erreur lors de la création du ticket ou de la transaction : {str(e)}")
                return redirect('voir_panier')
        else:
            messages.error(request, "Votre panier est vide.")
            return redirect('voir_panier')
    except Panier.DoesNotExist:
        messages.error(request, "Panier introuvable.")
        return redirect('voir_panier')

def send_confirmation_email(ticket):
    subject = 'Votre ticket pour les Jeux Olympiques'
    html_message = render_to_string('store/email_confirmation.html', {'ticket': ticket})
    plain_message = strip_tags(html_message)
    from_email = 'etudiantstudi@gmail.com'
    to = ticket.utilisateur.email

    #send_mail(subject, plain_message, from_email, [to], html_message=html_message)