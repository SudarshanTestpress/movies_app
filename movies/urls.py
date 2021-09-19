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
]
