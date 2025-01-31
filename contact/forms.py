from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = (
            'first_name', 'last_name', 'phone',
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        return super().clean()