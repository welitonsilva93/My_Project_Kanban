from django import forms
from .models import Task


class TaskForms(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'columns', 'descricao']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'forms-control',
                'placeholder': 'Digite o Titulo da Tarefa'
            }),
            'columns': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={
                'class': 'forms-control',
                'placeholder': 'Digite a descrição da Tarefa',
                'rows': 4,
                'cols': 47,
            })
        }