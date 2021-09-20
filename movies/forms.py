from django import forms
from django.forms import widgets

from .models import *


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


class MovieCreateForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = [
            "title",
            "subtitle",
            "directors",
            "studio",
            "released_date",
            "cover_image",
            "review",
            "genre",
            "asin",
        ]
        widgets = {
            "review": forms.Textarea(attrs={"rows": 4, "cols": 15}),
            "released_date": forms.DateInput(
                attrs={
                    "class": "datepicker",
                    "placeholder": "Select a date",
                    "type": "date",
                }
            ),
        }
