from django import forms
from django.contrib.auth.models import User
from .models import Cooperative, Membre
from django.contrib.auth.forms import UserCreationForm


class CooperativeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Cooperative
        fields = ['nom', 'adresse']

class MembreRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = Membre
        fields = ['adresse', 'numero_identification', 'cooperative']
    
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        membre = super().save(commit=False)
        membre.user = user
        if commit:
            membre.save()
        return membre
    
class CooperativeForm(forms.ModelForm):
    class Meta:
        model = Cooperative
        fields = ['nom', 'adresse']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'adresse': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Un compte avec cet email existe déjà.")
        return email
    
class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = ['adresse', 'numero_identification', 'cooperative']
        widgets = {
            'adresse': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_identification': forms.TextInput(attrs={'class': 'form-control'}),
            'cooperative': forms.Select(attrs={'class': 'form-control'}),
        }
