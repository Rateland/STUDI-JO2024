from django import forms
from store.models import *
from django.contrib.auth.models import User

class Ajout_Panier(forms.ModelForm):
    billet = forms.ModelChoiceField(queryset=OffreBillet.objects.all())
    quantité = forms.IntegerField(min_value=1, initial=1)

    class Meta:
        model = Achat
        fields = ['billet', 'quantité']