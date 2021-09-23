from django import forms
from django.forms import widgets

from studios.models import *


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
