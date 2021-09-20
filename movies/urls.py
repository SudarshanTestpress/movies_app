from django.urls import path

from . import views

urlpatterns = [
    path("studio/create", views.StudioCreateView.as_view(), name="create_studio"),
]
