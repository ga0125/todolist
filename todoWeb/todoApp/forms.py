from django import forms
import datetime

class TodoForm(forms.Form):
    dateDln = datetime.datetime.now().date()
    title = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class' : 'form-title', 'placeholder' : 'Insira o Título aqui...', 'aria-label' : 'task' ,'aria-describedby' : 'add-btn'}))
    desc = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class' : 'form-desc', 'placeholder' : 'Insira a descrição aqui...', 'aria-label' : 'task'  ,'aria-describedby' : 'add-btn'}))
    deadline = forms.DateTimeField(widget=forms.TextInput(attrs={'type' : 'date', 'class': 'deadline', 'aria-label': 'task','aria-describedby': 'add-btn', 'value': dateDln }))