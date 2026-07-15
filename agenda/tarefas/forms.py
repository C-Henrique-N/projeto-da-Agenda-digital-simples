from django import forms
from .models import Tarefa

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
        ('extrema', 'Extrema'), 
    ]

    prioridade = forms.ChoiceField(choices=PRIORIDADES)

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data', 'horario', 'prioridade']