from django import forms
from .models import Person

class PersonForm(forms.Form):
    region = forms.ModelChoiceField(
        queryset = Person.objects.all(),
    )