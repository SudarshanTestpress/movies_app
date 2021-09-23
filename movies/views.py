from django.db import models
from django.shortcuts import render
from django_filters.views import FilterView
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib import messages


from studios.models import Movies
from .forms import MovieCreateForm
from .filters import MovieFilter


class MovieListView(FilterView):
    model = Movies
    filterset_class = MovieFilter
    paginate_by = 6
    context_object_name = "movies"
    template_name = "movies/movie_list.html"


class MovieCreateView(CreateView):
    form_class = MovieCreateForm
    template_name = "movies/create_movie.html"
    success_url = reverse_lazy("movies:list")


class MovieUpdateView(UpdateView):
    model = Movies
    form_class = MovieCreateForm
    template_name = "movies/create_movie.html"
    success_url = reverse_lazy("movies:list")


class MovieDeleteView(DeleteView):
    model = Movies
    template_name = "movies/delete_movie.html"
    context_object_name = "movie"

    def get_success_url(self):
        messages.success(self.request, "movie was deleted successfully.")
        return reverse("movies:list")
