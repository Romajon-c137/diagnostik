from django import forms
from .models import FreeCall


class Form(forms.ModelForm):
    class Meta:
        model = FreeCall
        fields = ('full_name', 'e_mail', 'subject', 'phone_number', 'message')
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'e_mail': forms.TextInput(
                attrs={'placeholder': 'mail@email.com'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Your phone number'}),
            'message': forms.TextInput(attrs={'placeholder': 'Your message'}),
        }