from django.test import TestCase
from django.urls import reverse, resolve

from .models import Studio
from . import views


class Mixin:
    def create_studio(self, title="Test title", website="https://github.com"):
        return Studio.objects.create(title=title, website=website)


class TestStudioCreateView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("create_studio")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_studio_create_object(self):
        view = resolve("/studio/create")
        self.assertEquals(view.func.view_class, views.StudioCreateView)

    def test_presence_of_csrf(self):
        url = reverse("create_studio")
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_studio_save(self):

        self.client.post(
            "/studio/create",
            {
                "title": "I am a test studio",
                "website": "https://github.com",
            },
        )
        self.assertEqual(Studio.objects.last().title, "I am a test studio")


class TestStudioListView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("list_studio")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_studio_list_object(self):
        view = resolve("/studio")
        self.assertEquals(view.func.view_class, views.StudioListView)
