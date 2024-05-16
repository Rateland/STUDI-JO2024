from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from store.models import *
from store.QRcode import *

User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        email = request.POST.get("email")

        # Validation des mots de passe
        if password != password_confirm:
            messages.error(request, 'Les mots de passe ne correspondent pas.')
            return render(request, 'accounts/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d’utilisateur est déjà pris.')
            return render(request, 'accounts/signup.html')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=prenom,
            last_name=nom,
            email=email
        )
        login(request, user)
        return redirect('accueil')

    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user:
            user = authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                return redirect('accueil')

        messages.error(request, 'Courriel ou mot de passe incorrect.')
        return render(request, 'accounts/login.html')
    
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('accueil')