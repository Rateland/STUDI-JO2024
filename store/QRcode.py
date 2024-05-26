import uuid
import qrcode
import json
from io import BytesIO
from django.core.files import File
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Génère un identifiant unique
def generate_unique_id():
    return str(uuid.uuid4())

# Simule un paiement en renvoyant un statut et un identifiant de transaction
def simulate_payment(amount):
    transaction_id = generate_unique_id()
    status = "réussi" if amount > 0 else "échoué"
    return transaction_id, status

# Génère un code QR pour un ticket
def generate_qr_code(ticket):
    data = {
        'transaction_id': str(ticket.transaction.id),
        'utilisateur': ticket.utilisateur.username,
        'montant_total': str(ticket.montant_total),
        'achats': [
            {
                'billet': achat.billet.nom,
                'quantité': achat.quantité,
                'prix': str(achat.billet.prix)
            }
            for achat in ticket.achats.all()
        ],
        'date_creation': ticket.date_creation.isoformat()
    }

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json.dumps(data))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    ticket.qr_code.save(f'{ticket.transaction.id}.png', File(buffer), save=False)
    ticket.save()

def verifier_ticket(ticket):
    assert ticket.transaction is not None, "Transaction manquante"
    assert ticket.utilisateur is not None, "Utilisateur manquant"
    assert ticket.montant_total > 0, "Montant total incorrect"
    assert ticket.achats.exists(), "Aucun achat associé au ticket"
    assert ticket.qr_code, "Code QR manquant"

def envoyer_email_confirmation(ticket, destinataire):
    sujet = 'Confirmation de votre achat'
    corps = render_to_string('store/email_confirmation.html', {'ticket': ticket})

    email = EmailMessage(
        sujet,
        corps,
        'votre-adresse@example.com',
        [destinataire]
    )
    if ticket.qr_code:
        email.attach_file(ticket.qr_code.path)
    email.send()