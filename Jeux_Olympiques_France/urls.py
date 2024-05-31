from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import *
from accounts.views import *
from Jeux_Olympiques_France import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# note pour retravailler ça : path('lechemin/', lavue, name="lechemin")
urlpatterns = [
    path('', accueil, name='accueil'),
    path('mentions_legales', mentions_legales, name="mentions_legales"),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('client/', client_page, name='client_page'),
    path('client/ticket/<int:ticket_id>/telecharger/', telecharger_ticket, name='telecharger_ticket'),
    path('client/ticket/<int:ticket_id>/supprimer/', supprimer_ticket, name='supprimer_ticket'),
    path('epreuves/<str:slug>/', epreuves_detail, name='epreuves'),
    path('epreuves/<str:epreuve_slug>/<str:billet_slug>/ajout_panier', ajout_panier, name="panier_epreuves"),
    path('epreuves/', liste_epreuves, name="liste_epreuves"),
    path('billets/<str:slug>/', billets_detail, name="billets"),
    path('liste_offres/', liste_billets, name='liste_offres'),
    path('panier/', voir_panier, name='voir_panier'),
    path('panier/supprimer/<int:achat_id>/', supprimer_achat, name='supprimer_achat'),
    path('paiement/', paiement, name='paiement'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('clear_pdf_downloaded_flag/', clear_pdf_downloaded_flag, name='clear_pdf_downloaded_flag'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)