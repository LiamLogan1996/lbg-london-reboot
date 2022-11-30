from django import forms
from .models import Input
from django.core.exceptions import ValidationError

def validate_positive(value):
   if value < 0:
        raise ValidationError(('%(value) is not a positive number. Please try again with 0 or a positive number.'),params={'value': value})

class InputForm(forms.ModelForm):
    salary_input = forms.FloatField(validators=[validate_positive])

    class Meta:
        model = Input
        fields = ('salary_input',)
