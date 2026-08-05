from django import forms
from .models import Tarefa

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class TarefaForm(forms.ModelForm):
    data = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    horario = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'})
    )

    PRIORIDADES = [
        ('baixa', 'Baixa'),
        ('média', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]

    prioridade = forms.ChoiceField(choices=PRIORIDADES)

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data', 'horario', 'prioridade']


class CadastroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "placeholder": "Digite seu nome de usuário"
        })

        self.fields["password1"].widget.attrs.update({
            "placeholder": "Digite sua senha"
        })

        self.fields["password2"].widget.attrs.update({
            "placeholder": "Confirme sua senha"
        })

        self.fields["username"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None