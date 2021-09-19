from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages


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


class StudioUpdateView(UpdateView):
    model = Studio
    fields = ["title", "website"]
    template_name = "movies/create_studio.html"
    success_url = reverse_lazy("list_studio")


class StudioDeleteView(DeleteView):
    model = Studio
    template_name = "movies/delete_studio.html"
    context_object_name = "studio"

    def get_success_url(self):
        messages.success(self.request, "Studio was deleted successfully.")
        return reverse("list_studio")
