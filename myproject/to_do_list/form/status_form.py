from django import forms

from to_do_list.models import Task



class StatusForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        min_length=3,
        #required=True,
        label='Название жанра',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название жанра'
        })
    )
    description = forms.CharField(
        max_length=500,
        min_length=3,
        #required=True,
        label='Описание',
        widget=forms.Textarea(attrs={
            'rows': 5,
            'class': 'form-control'
        })
    )