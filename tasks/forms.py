from tkinter import Widget
from django import forms
from .models import Task

#para fazer inserção de dados no banco no django via form é necessario criar um arquivo 'forms.py'
#e aqui estabelecer toda a logica necessaria pra insercao desses dados no banco

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task # especifa de qual model esse form será
        fields = ('title', 'description') # fala pra form que vc vai estar inserindo esses dados no banco atraves do form (addtask.html)
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}), # add class para os inputs para nao ficar feiao padrao do django
            'description' : forms.Textarea(attrs={'class':'form-control'}),
        }