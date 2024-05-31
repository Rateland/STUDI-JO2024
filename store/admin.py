from django.contrib import admin
from .models import *

class OffreBilletAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'formatted_stock', 'nombre_personnes', 'epreuve')

class AchatInline(admin.TabularInline):
    model = Achat
    extra = 1  # Aucune ligne supplémentaire
    can_delete = True

class PanierAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'acheté', 'date_achat')
    search_fields = ('utilisateur__username',)
    list_filter = ('acheté',)

class AchatAdmin(admin.ModelAdmin):
    list_display = ('billet', 'utilisateur', 'quantité', 'epreuve')
    search_fields = ('utilisateur__username', 'billet__titre')
    list_filter = ('epreuve',)

# Register your models here.
admin.site.register(OffreBillet, OffreBilletAdmin)
admin.site.register(Epreuve)
admin.site.register(Achat, AchatAdmin)
admin.site.register(Panier, PanierAdmin)