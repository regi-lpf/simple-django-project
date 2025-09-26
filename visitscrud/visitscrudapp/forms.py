from django import forms
from .models import Visit

class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

        labels = {
            'id': 'Visit ID',
            'name': 'Visit Name',
            'place': 'Place',
            'time': 'Time',
            'date': 'Date',
            'description': 'Description',
            'rating': 'Rating',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'ex. John Doe', 'maxlength': '50'}),
            'place': forms.TextInput(attrs={'placeholder': 'ex. Blumenau', 'maxlength': '100'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'required': 'true'}),
            'date': forms.DateInput(attrs={'type': 'date', 'required': 'true'}),
            'description': forms.Textarea(attrs={'placeholder': 'Enter a description of the visit', 'maxlength': '300'}),
            'rating': forms.NumberInput(attrs={'min': '0', 'max': '10', 'required': 'true'}),
        }
