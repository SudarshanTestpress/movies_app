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
        view = resolve("/studios/create")
        self.assertEquals(view.func.view_class, views.StudioCreateView)

    def test_presence_of_csrf(self):
        url = reverse("create_studio")
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_studio_save(self):

        self.client.post(
            "/studios/create",
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
        view = resolve("/studios/")
        self.assertEquals(view.func.view_class, views.StudioListView)


class TestStudioUpdateView(TestCase, Mixin):
    def setUp(self):
        self.studio = self.create_studio()

    def test_page_serve_successful(self):
        url = reverse("update_studio", args=[self.studio.slug])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_studio_update_object(self):
        studio_slug = self.studio.slug
        view = resolve(f"/studios/{studio_slug}/update")
        self.assertEquals(view.func.view_class, views.StudioUpdateView)

    def test_presence_of_csrf(self):
        url = reverse("update_studio", args=[self.studio.slug])
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_studio_save(self):
        studio_slug = self.studio.slug

        self.client.post(
            f"/studios/{studio_slug}/update",
            {
                "title": "I am a test studio upated",
                "website": "https://github.com",
            },
        )
        self.studio.refresh_from_db()
        self.assertEqual(self.studio.title, "I am a test studio upated")


class TestStudioDeleteView(TestCase, Mixin):
    def setUp(self):
        self.studio = self.create_studio()

    def test_page_serve_successful(self):
        url = reverse("delete_studio", args=[self.studio.slug])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_studio_delete_object(self):
        studio_slug = self.studio.slug
        view = resolve(f"/studios/{studio_slug}/delete")
        self.assertEquals(view.func.view_class, views.StudioDeleteView)
