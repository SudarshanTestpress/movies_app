from django.shortcuts import render
from django.views.generic import CreateView


from .models import Studio


class StudioCreateView(CreateView):
    model = Studio
    fields = ["title", "website"]
    template_name = "movies/create_studio.html"
    success_url = "#"
