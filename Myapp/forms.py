from django import forms
from .models import Cartao

class CartaoForm(forms.ModelForm):
    class Meta:
        model = Cartao
        fields = ['cpf', 'email', 'numero_cartao', 'nome_do_cartao', 'validade', 'cvv']