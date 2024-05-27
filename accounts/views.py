from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from .forms import *
from store.models import *
from store.QRcode import *
from django.urls import reverse_lazy

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
            return render(request, 'accounts/signup.jinja2')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ce nom d’utilisateur est déjà pris.')
            return render(request, 'accounts/signup.jinja2')

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=prenom,
            last_name=nom,
            email=email
        )
        login(request, user)
        return redirect('accueil')

    return render(request, 'accounts/signup.jinja2')

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
        return render(request, 'accounts/login.jinja2')
    
    return render(request, 'accounts/login.jinja2')

@login_required
def client_page(request):
    if request.method == "POST":
        name_form = NameForm(request.POST, instance=request.user)
        email_form = EmailForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)

        if 'name_submit' in request.POST and name_form.is_valid():
            name_form.save()
            messages.success(request, "Votre nom et prénom ont été mis à jour avec succès.")
            return redirect('client_page')

        if 'email_submit' in request.POST and email_form.is_valid():
            email_form.save()
            messages.success(request, "Votre adresse e-mail a été mise à jour avec succès.")
            return redirect('client_page')

        if 'password_submit' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Votre mot de passe a été mis à jour avec succès.")
            return redirect('client_page')
    else:
        name_form = NameForm(instance=request.user)
        email_form = EmailForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'accounts/client_page.jinja2', {
        'name_form': name_form,
        'email_form': email_form,
        'password_form': password_form
    })

def logout_user(request):
    logout(request)
    return redirect('accueil')