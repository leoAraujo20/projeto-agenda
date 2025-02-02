from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone", "email", "description", "category", "picture")
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'phone': 'Número de Telefone',
            'email': 'E-mail',
            'description': 'Descrição',
            'category': 'Categoria',
            "picture": "Foto"
        }
    
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name and first_name == last_name:
            self.add_error(None, "Primeiro nome não pode ser igual ao sobrenome")
        
        return cleaned_data

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2",)
        labels = {
            "last_name": "Sobrenome",
        }
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        if User.objects.filter(email=email).exists():
            self.add_error("email", ValidationError("Este e-mail já está em uso"))
        
        return email

class UserLoginForm(AuthenticationForm):
    pass