from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages


from studios.models import Director
from .forms import DirectorCreateForm


class DirectorListView(ListView):
    model = Director
    paginate_by = 6
    context_object_name = "directors"
    template_name = "directors/director_list.html"


class DirectorCreateView(CreateView):
    form_class = DirectorCreateForm
    template_name = "directors/create_director.html"
    success_url = reverse_lazy("directors:list")


class DirectorUpdateView(UpdateView):
    model = Director
    form_class = DirectorCreateForm
    template_name = "directors/create_director.html"
    success_url = reverse_lazy("directors:list")


class DirectorDeleteView(DeleteView):
    model = Director
    template_name = "directors/delete_director.html"
    context_object_name = "director"

    def get_success_url(self):
        messages.success(self.request, "Director Profile was deleted successfully.")
        return reverse("directors:list")
