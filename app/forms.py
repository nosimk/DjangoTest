from app.models import Person
from django import forms
from django.forms.widgets import TextInput, ClearableFileInput


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Enter your Name',}),
            'title': TextInput(attrs={'class': 'form-control',
                                      'placeholder': 'Enter your Title',}),
            'description': TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Enter your Description',}),
            'image': ClearableFileInput(attrs={'class': 'form-control',
                                               'title':'Upload your Image',
                                               'style' : 'width:100',
                                               'accept':'image/*',}),
        }