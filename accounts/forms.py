from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

CustomUser = get_user_model()

class ClientForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class NameForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name']

class UsernameForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username']

class EmailForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email']

class PhoneForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['phone']

class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = CustomUser
        fields = ['password']