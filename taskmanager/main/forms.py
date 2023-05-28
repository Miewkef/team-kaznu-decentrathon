from .models import Price
from django.forms import ModelForm, TextInput


class PriceForm(ModelForm):
    class Meta:
        model = Price
        fields = ["server_title", "price"]
        widgets = {
            "server_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Стоимость'
            }),
        }