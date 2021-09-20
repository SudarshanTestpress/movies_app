from django.urls import path

from . import views

urlpatterns = [
    path("studio/create", views.StudioCreateView.as_view(), name="create_studio"),
    path("studio", views.StudioListView.as_view(), name="list_studio"),
    path(
        "studio/<slug:slug>/update",
        views.StudioUpdateView.as_view(),
        name="update_studio",
    ),
    path(
        "studio/<slug:slug>/delete",
        views.StudioDeleteView.as_view(),
        name="delete_studio",
    ),
    path("director", views.DirectorListView.as_view(), name="list_director"),
    path("director/create", views.DirectorCreateView.as_view(), name="create_director"),
    path(
        "director/<str:pk>/update",
        views.DirectorUpdateView.as_view(),
        name="update_director",
    ),
    path(
        "director/<str:pk>/delete",
        views.DirectorDeleteView.as_view(),
        name="delete_director",
    ),
    path("movie", views.MovieListView.as_view(), name="list_movie"),
    path("movie/create", views.MovieCreateView.as_view(), name="create_movie"),
]
