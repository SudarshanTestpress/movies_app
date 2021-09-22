from django.test import TestCase
from django.urls import reverse, resolve

from studios.models import Director
from . import views


class Mixin:
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


class TestDirectorListView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("director:list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_director_list_object(self):
        view = resolve("/directors/")
        self.assertEquals(view.func.view_class, views.DirectorListView)


class TestDirectorCreateView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("director:create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_director_create_object(self):
        view = resolve("/directors/create")
        self.assertEquals(view.func.view_class, views.DirectorCreateView)

    def test_presence_of_csrf(self):
        url = reverse("director:create")
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_director_save(self):

        self.client.post(
            "/directors/create",
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


class TestDirectorUpdateView(TestCase, Mixin):
    def setUp(self):
        self.director = self.create_director()

    def test_page_serve_successful(self):
        url = reverse("director:update", args=[self.director.pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_director_update_object(self):
        director_slug = self.director.id
        view = resolve(f"/directors/{director_slug}/update")
        self.assertEquals(view.func.view_class, views.DirectorUpdateView)

    def test_presence_of_csrf(self):
        url = reverse("director:update", args=[self.director.pk])
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_director_save(self):
        director_slug = self.director.pk

        self.client.post(
            f"/directors/{director_slug}/update",
            {
                "first_name": "Mack",
                "middle_name": "Matthew",
                "last_name": "Doe",
                "phone_number": "+919444161121",
                "birthdate": "2021-5-8",
                "website": "http://127.0.0.1:8000/director",
                "gender": "M",
            },
        )
        self.director.refresh_from_db()
        self.assertEqual(self.director.first_name, "Mack")
        self.assertEqual(self.director.last_name, "Doe")


class TestDirectorDeleteView(TestCase, Mixin):
    def setUp(self):
        self.director = self.create_director()

    def test_page_serve_successful(self):
        url = reverse("director:delete", args=[self.director.pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_director_delete_object(self):
        director_pk = self.director.pk
        view = resolve(f"/directors/{director_pk}/delete")
        self.assertEquals(view.func.view_class, views.DirectorDeleteView)


class TestDirectorDetailView(TestCase, Mixin):
    def setUp(self):
        self.director = self.create_director()

    def test_page_serve_successful(self):
        url = reverse("directors:detail", args=[self.director.pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_event_detail_object(self):
        view = resolve(f"/directors/{self.director.pk}/detail")
        self.assertEquals(view.func.view_class, views.DirectorDetailView)
