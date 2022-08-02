from django import forms
from .models import Automobile


class AutoForm(forms.ModelForm):
    class Meta:
        model = Automobile
        fields = [
            'model',
            'brand',
            'photo'
        ]

        widgets = {
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите модель автомобиля'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),

        }
