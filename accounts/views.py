from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.

User = get_user_model()
def signup(request):
    if request.method == "POST": # Traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html', {
                'error': 'Ce nom d’utilisateur est déjà pris.'
            })

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('accueil')
    
    return render(request, 'accounts/signup.html')

def login_user(request): # Connecter l’utilisateur
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('accueil')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Nom d’utilisateur ou mot de passe incorrect.'
            })
        
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    return redirect('accueil')