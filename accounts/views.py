from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import get_user_model, login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib import messages
from .forms import *
from .models import *
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
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            user = authenticate(username=user.username, password=password)
            if user:
                login(request, user)
                return redirect('accueil')

        messages.error(request, 'Nom d’utilisateur ou mot de passe incorrect.')
        return render(request, 'accounts/login.html')
    
    return render(request, 'accounts/login.html')

@login_required
def client_page(request):
    user = request.user
    if request.method == "POST":
        name_form = NameForm(request.POST, instance=user)
        username_form = UsernameForm(request.POST, instance=user)
        email_form = EmailForm(request.POST, instance=user)
        phone_form = PhoneForm(request.POST, instance=user)
        password_form = CustomPasswordChangeForm(user=user, data=request.POST)

        if 'name_submit' in request.POST and name_form.is_valid():
            name_form.save()
            messages.success(request, "Votre nom et prénom ont été mis à jour avec succès.")
            return redirect('client_page')

        if 'username_submit' in request.POST and username_form.is_valid():
            username_form.save()
            messages.success(request, "Votre nom d'utilisateur a été mis à jour avec succès.")
            return redirect('client_page')

        if 'email_submit' in request.POST and email_form.is_valid():
            email_form.save()
            messages.success(request, "Votre adresse e-mail a été mise à jour avec succès.")
            return redirect('client_page')

        if 'phone_submit' in request.POST and phone_form.is_valid():
            phone_form.save()
            messages.success(request, "Votre numéro de téléphone a été mis à jour avec succès.")
            return redirect('client_page')

        if 'password_submit' in request.POST and password_form.is_valid():
            user = password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Votre mot de passe a été mis à jour avec succès.")
            return redirect('client_page')
    else:
        name_form = NameForm(instance=user)
        username_form = UsernameForm(instance=user)
        email_form = EmailForm(instance=user)
        phone_form = PhoneForm(instance=user)
        password_form = CustomPasswordChangeForm(user=user)

    tickets = Ticket.objects.filter(utilisateur=user, payé=True)

    return render(request, 'accounts/client_page.html', {
        'name_form': name_form,
        'username_form': username_form,
        'email_form': email_form,
        'phone_form': phone_form,
        'password_form': password_form,
        'tickets': tickets,
    })

@login_required
def clear_pdf_downloaded_flag(request):
    if 'pdf_downloaded' in request.session:
        del request.session['pdf_downloaded']
    return HttpResponse(status=204)

@login_required
def supprimer_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id, utilisateur=request.user)
    if request.method == "POST":
        ticket.delete()
        messages.success(request, "Le ticket a été supprimé avec succès.")
        return redirect('client_page')
    return render(request, 'accounts/confirm_delete.html', {'ticket': ticket})

def logout_user(request):
    logout(request)
    return redirect('accueil')