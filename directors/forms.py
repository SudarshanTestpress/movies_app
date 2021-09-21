from django import forms
from django.forms import widgets

from studios.models import *


class DirectorCreateForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "phone_number",
            "birthdate",
            "gender",
            "website",
        ]
