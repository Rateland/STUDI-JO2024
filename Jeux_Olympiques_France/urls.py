"""
URL configuration for Jeux_Olympiques_France project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from store.views import *
from accounts.views import *
from Jeux_Olympiques_France import settings

# note pour retravailler ça : path('lechemin/', lavue, name="lechemin")
urlpatterns = [
    path('', accueil, name='accueil'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('logout/', logout_user, name="logout"),
    path('login/', login_user, name="login"),
    path('epreuves/<str:slug>/', epreuves_detail, name="epreuves"),
    path('epreuves/<str:slug>/ajout_panier', ajout_panier, name="panier_epreuves"),
    path('epreuves/', liste_epreuves, name="liste_epreuves"),
    path('billets/<str:slug>/', billets_detail, name="billets"),
    path('billets/<str:slug>/ajout_panier', ajout_panier, name="panier_billets"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)