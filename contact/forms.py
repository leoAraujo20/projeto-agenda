from django import forms
from contact.models import Contact
from django.core.exceptions import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("first_name", "last_name", "phone", "email", "description", "category")
        labels = {
            'first_name': 'Primeiro Nome',
            'last_name': 'Sobrenome',
            'phone': 'Número de Telefone',
            'email': 'E-mail',
            'description': 'Descrição',
            'category': 'Categoria',
        }
    
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")

        if first_name and last_name and first_name == last_name:
            self.add_error(None, "Primeiro nome não pode ser igual ao sobrenome")
        
        return cleaned_data