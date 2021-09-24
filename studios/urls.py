from django.urls import path

from . import views

app_name = "studios"

urlpatterns = [
    path("create", views.StudioCreateView.as_view(), name="create"),
    path("", views.StudioListView.as_view(), name="list"),
    path(
        "<slug:slug>/update",
        views.StudioUpdateView.as_view(),
        name="update",
    ),
    path(
        "<slug:slug>/delete",
        views.StudioDeleteView.as_view(),
        name="delete",
    ),
]
