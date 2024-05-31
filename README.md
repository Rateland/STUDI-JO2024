# Projet JO 2024

## Introduction
Ce projet vise à fournir une plateforme de gestion des achats et des événements pour les Jeux Olympiques 2024.

## Installation
### Prérequis
- Python 3.x
- Django 4.x
- PostgreSQL

### Étapes d'Installation
    1. Cloner le dépôt
        'git clone https://github.com/Rateland/STUDI-JO2024.git'
        'cd STUDI-JO2024'

    2. Créer et activer un environnement virtuel
        'python -m venv env'
        'source env/bin/activate' OU 'env\Scripts\activate'

    3. Installer les dépendances
        'pip install -r requirements.txt'

    4. Configurer la base de données
        'python manage.py migrate'

    5. Créer un superutilisateur
        'python manage.py createsuperuser'
        (Dans le lore : Admin, MdP : 4dministrateur@JOF)

    6. Lancer le serveur de développement
        'python manage.py runserver'

### Configuration des Variables d'Environnement
    Créez un fichier .env à la racine du projet avec le contenu suivant :

        DATABASE_URL=postgres://username:password@localhost:5432/dbname
        EMAIL_HOST_USER=example@gmail.com
        EMAIL_HOST_PASSWORD=yourpassword
        SECRET_KEY=your_secret_key
        DEBUG=True

### Guide de Développement
**Structure du Projet**
- store/
  - models.py
  - views.py
  - tests/
    - test_views.py
- accounts/
  - models.py
  - views.py
  - tests/
    - test_views.py
- templates/
  - base.html
  - store/
    - ...
  - accounts/
    - ...

**Modèles de Données**
Epreuve
titre : CharField
slug : SlugField

### Utilisation
**Interface Utilisateur**
L'interface utilisateur permet aux utilisateurs de s'inscrire, de se connecter, de parcourir les événements, d'ajouter des billets au panier et de finaliser les achats.

**Interface d'Administration**
L'interface d'administration de Django permet de gérer les utilisateurs, les événements, les offres de billets, et les commandes.

### Tests
**Structure des Tests**
Les tests sont organisés par application dans les répertoires store/tests/ et accounts/tests/.

**Exécution des Tests**
Pour exécuter les tests, utilisez la commande suivante :
    'python manage.py test'

**Tests Automatisés**
Créez un fichier .github/workflows/django.yml avec le contenu suivant pour configurer l'intégration continue avec GitHub Actions :

name: Django CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    services:
      postgres:
        image: postgres:11
        env:
          POSTGRES_DB: jo2024
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports:
          - 5432:5432
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    env:
      DATABASE_URL: postgres://postgres:postgres@localhost:5432/jo2024

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.8'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run migrations
      run: python manage.py migrate
    - name: Run tests
      run: python manage.py test


### Déploiement
**Local**
Pour déployer localement, suivez les instructions d'installation ci-dessus.

**Heroku**
a. Créez une application Heroku
b. Configurez les variables d'environnement dans le dashboard Heroku
c. Poussez le code vers Heroku
    'git push heroku main'

### Maintenance

**Contribuer**
Pour contribuer, veuillez soumettre une pull request avec une description détaillée de vos modifications.

**FAQ**
Q: Comment configurer la base de données ?
A: Consultez la section "Installation et Configuration".

Q: Comment exécuter les tests ?
A: Utilisez la commande python manage.py test.

### Références
Django Documentation
Heroku Documentation
perl
Copier le code

### Suggestions de Tests et Automatisation
1. **Tests unitaires et d'intégration** :
    - Placez les tests spécifiques aux fonctionnalités de chaque application dans leurs répertoires respectifs : `store/tests/` et `accounts/tests/`.
    - Ajoutez des tests pour les modèles, les vues, les formulaires et les URL.
    - Exemple de test pour `store` :
    from django.test import TestCase
    from .models import Epreuve

    class EpreuveModelTest(TestCase):
        def test_string_representation(self):
            epreuve = Epreuve(titre="Course")
            self.assertEqual(str(epreuve), epreuve.titre)

### Automatisation des Tests
Les tests peuvent être automatisés en configurant GitHub Actions pour exécuter les tests à chaque push ou pull request. Cela garantit que le code est toujours testé et que les régressions sont rapidement détectées.