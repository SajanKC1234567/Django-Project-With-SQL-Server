from django import forms
from datetime import datetime
from .models import Registration
from sqlite3 import *


class AvailabilityForm(forms.Form):
    Register_DateTime = forms.DateField(
        required=True, input_formats=["%Y-%m-%d", "%Y-%m-%d"], widget=forms.DateInput(attrs={'type': 'date-local'}))

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"