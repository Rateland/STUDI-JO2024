import uuid
import qrcode
import json
from io import BytesIO
from django.core.files import File
from django.template.loader import render_to_string
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from store.models import *
from django.conf import settings

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

def create_ticket_pdf(ticket):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Vérification de la première épreuve dans les achats
    first_achat = ticket.achats.first()
    if first_achat and first_achat.epreuve:
        epreuve_titre = first_achat.epreuve.titre
        offre_nom = first_achat.billet.nom
    else:
        epreuve_titre = "Épreuve inconnue"
        offre_nom = "Offre inconnue"

    # En-tête avec le nom de l'épreuve
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 50, f"Epreuve: {epreuve_titre}")

    # Sous-titre avec le type d'offre
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 70, f"Billet: {offre_nom}")

    # Ajouter le QR code au PDF
    if ticket.qr_code:
        img_path = ticket.qr_code.path
        c.drawImage(img_path, width - 200, height - 200, width=150, height=150)

    # Détails du ticket
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, f"Ticket ID: {ticket.id}")
    c.drawString(100, height - 120, f"Utilisateur: {ticket.utilisateur.username}")
    c.drawString(100, height - 140, f"Montant total: {ticket.montant_total} €")

    # Pied de page avec l'adresse du site
    c.setFont("Helvetica", 10)
    c.drawString(100, 30, f"Site web: {settings.SITE_URL}")

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer