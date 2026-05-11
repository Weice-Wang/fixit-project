from django import forms
from .models import Maintaining, Tag

class MaintainingForm(forms.ModelForm):
    class Meta:
        model = Maintaining
        fields = ['date', 'repair_type', 'description', 'cost']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

        widgets = {
            'color': forms.TextInput(attrs={
                'type': 'color'
            })
        }