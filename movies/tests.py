from django.test import TestCase
from django.urls import reverse, resolve

from .models import Studio, Director
from . import views


class Mixin:
    def create_studio(self, title="Test title", website="https://github.com"):
        return Studio.objects.create(title=title, website=website)

    def create_director(
        self,
        first_name="John",
        middle_name="Matthew",
        last_name="Doe",
        phone_number="+919444161121",
        birthdate="2021-5-8",
        website="http://127.0.0.1:8000/director",
        gender="Male",
    ):
        return Director.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            phone_number=phone_number,
            birthdate=birthdate,
            website=website,
            gender=gender,
        )


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


class TestStudioUpdateView(TestCase, Mixin):
    def setUp(self):
        self.studio = self.create_studio()

    def test_page_serve_successful(self):
        url = reverse("update_studio", args=[self.studio.slug])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_studio_update_object(self):
        studio_slug = self.studio.slug
        view = resolve(f"/studio/{studio_slug}/update")
        self.assertEquals(view.func.view_class, views.StudioUpdateView)

    def test_presence_of_csrf(self):
        url = reverse("update_studio", args=[self.studio.slug])
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_studio_save(self):
        studio_slug = self.studio.slug

        self.client.post(
            f"/studio/{studio_slug}/update",
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
        view = resolve(f"/studio/{studio_slug}/delete")
        self.assertEquals(view.func.view_class, views.StudioDeleteView)


class TestDirectorListView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("list_director")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_studio_list_object(self):
        view = resolve("/director")
        self.assertEquals(view.func.view_class, views.DirectorListView)


class TestDirectorCreateView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("create_director")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_director_create_object(self):
        view = resolve("/director/create")
        self.assertEquals(view.func.view_class, views.DirectorCreateView)

    def test_presence_of_csrf(self):
        url = reverse("create_director")
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_director_save(self):

        self.client.post(
            "/director/create",
            {
                "first_name": "John",
                "middle_name": "Matthew",
                "last_name": "Doe",
                "phone_number": "+919444161121",
                "birthdate": "2021-5-8",
                "website": "http://127.0.0.1:8000/director",
                "gender": "M",
            },
        )
        self.assertEqual(Director.objects.last().first_name, "John")
