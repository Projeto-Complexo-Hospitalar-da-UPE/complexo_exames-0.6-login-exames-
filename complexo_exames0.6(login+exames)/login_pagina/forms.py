from django import forms
from django.forms import ModelForm
from .models import exames

class ExamesForm(ModelForm):
    class Meta:
        model = exames
        fields = ('paciente', 'nome_exame', 'data_realizacao', 'descricao', 'concluido', 'arquivo')

        widgets = {
            #'paciente': forms.ModelChoiceField(queryset=exames.objects.all(), attrs={'class':'form-control', 'id':'exampleFormControlSelect1', 'placeholder':'Nome do paciente'}),
            'nome_exame': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nome do exame'}),
            'data_realizacao': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'descricao': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descrição do exame'}),
            'concluido': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'arquivo': forms.FileInput(attrs={'class':'form-control'}),
        }