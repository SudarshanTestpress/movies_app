from django.urls import path

from . import views

app_name = "directors"

urlpatterns = [
    path("", views.DirectorListView.as_view(), name="list"),
    path("create", views.DirectorCreateView.as_view(), name="create"),
    path(
        "<str:pk>/update",
        views.DirectorUpdateView.as_view(),
        name="update",
    ),
    path(
        "<str:pk>/delete",
        views.DirectorDeleteView.as_view(),
        name="delete",
    ),
    path(
        "<str:pk>/detail",
        views.DirectorDetailView.as_view(),
        name="detail",
    ),
]
