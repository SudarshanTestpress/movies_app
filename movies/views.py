from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy


from .models import Studio


class StudioCreateView(CreateView):
    model = Studio
    fields = ["title", "website"]
    template_name = "movies/create_studio.html"
    success_url = reverse_lazy("list_studio")


class StudioListView(ListView):
    model = Studio
    paginate_by = 9
    context_object_name = "studios"
    template_name = "movies/studio_list.html"
