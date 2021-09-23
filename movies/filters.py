import django_filters
from django_filters import rest_framework as filters
from django import forms
from taggit.models import Tag


from studios.models import Movies


class MovieFilter(django_filters.FilterSet):
    genre = filters.ModelMultipleChoiceFilter(queryset=Tag.objects.all())

    class Meta:
        model = Movies
        fields = ["directors", "genre", "studio"]
