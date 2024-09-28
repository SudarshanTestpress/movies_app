from django.urls import path

from . import views

app_name = "movies"

urlpatterns = [
    path("", views.MovieListView.as_view(), name="list"),
    path("create", views.MovieCreateView.as_view(), name="create"),
    path(
        "<slug:slug>/update",
        views.MovieUpdateView.as_view(),
        name="update",
    ),
    path(
        "<slug:slug>/delete",
        views.MovieDeleteView.as_view(),
        name="delete",
    ),
    path(
        "<slug:slug>/detail",
        views.MovieDetailView.as_view(),
        name="detail",
    ),
]
