from django import forms
from .models import *


class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ['phone_number', 'email', 'address']
        
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            
        }