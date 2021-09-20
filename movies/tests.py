from django.test import TestCase
from django.urls import reverse, resolve

from .models import Movies, Studio, Director
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

    def create_movie(
        self,
        directors=None,
        title="Interstellar",
        subtitle="http://127.0.0.1:8000/director",
        studio=None,
        released_date="2021-5-8",
        cover_image="Users/admin/Desktop/Screenshot 2021-09-09 at 5.10.43 PM.png",
        review="Good movie",
        asin=12334,
    ):

        if studio == None:
            studio = self.create_studio()

        if directors == None:
            director = self.create_director()

        movie = Movies.objects.create(
            title=title,
            subtitle=subtitle,
            cover_image=cover_image,
            studio=studio,
            released_date=released_date,
            review=review,
            asin=asin,
        )
        movie.directors.add(director)
        return movie


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


class TestDirectorUpdateView(TestCase, Mixin):
    def setUp(self):
        self.director = self.create_director()

    def test_page_serve_successful(self):
        url = reverse("update_director", args=[self.director.pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_director_update_object(self):
        director_slug = self.director.id
        view = resolve(f"/director/{director_slug}/update")
        self.assertEquals(view.func.view_class, views.DirectorUpdateView)

    def test_presence_of_csrf(self):
        url = reverse("update_director", args=[self.director.pk])
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_director_save(self):
        director_slug = self.director.pk

        self.client.post(
            f"/director/{director_slug}/update",
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
        url = reverse("delete_director", args=[self.director.pk])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_director_delete_object(self):
        director_pk = self.director.pk
        view = resolve(f"/director/{director_pk}/delete")
        self.assertEquals(view.func.view_class, views.DirectorDeleteView)


class TestMovieListView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("list_movie")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_movie_list_object(self):
        view = resolve("/movie")
        self.assertEquals(view.func.view_class, views.MovieListView)


class TestMovieCreateView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("create_movie")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_movie_create_object(self):
        view = resolve("/movie/create")
        self.assertEquals(view.func.view_class, views.MovieCreateView)

    def test_presence_of_csrf(self):
        url = reverse("create_movie")
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_director_save(self):
        director = self.create_director()
        studio = self.create_studio()

        self.client.post(
            "/movie/create",
            {
                "title": "dunkirk",
                "subtitle": "http://127.0.0.1:8000/director",
                "directors": [director.id],
                "studio": studio.id,
                "released_date": "2021-5-8",
                "cover_image": "Users/admin/Desktop/Screenshot 2021-09-09 at 5 10.43 PM.png",
                "review": "Good movie",
                "asin": 12334,
            },
        )
        self.assertEqual(Movies.objects.last().title, "dunkirk")


class TestMovieUpdateView(TestCase, Mixin):
    def setUp(self):
        self.movie = self.create_movie()

    def test_page_serve_successful(self):
        url = reverse("update_movie", args=[self.movie.slug])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_movie_create_object(self):
        movie_slug = self.movie.slug
        view = resolve(f"/movie/{movie_slug}/update")
        self.assertEquals(view.func.view_class, views.MovieUpdateView)

    def test_presence_of_csrf(self):
        url = reverse("update_movie", args=[self.movie.slug])
        response = self.client.get(url)
        self.assertContains(response, "csrfmiddlewaretoken")

    def test_director_save(self):
        director = self.create_director(phone_number="+919444062231")

        self.client.post(
            f"/movie/{self.movie.slug}/update",
            {
                "title": "dunkirk",
                "subtitle": "http://127.0.0.1:8000/director",
                "directors": [director.id],
                "studio": self.movie.studio.id,
                "released_date": "2021-5-8",
                "cover_image": "Users/admin/Desktop/Screenshot 2021-09-09 at 5 10.43 PM.png",
                "review": "Good movie",
                "asin": 12334,
            },
        )
        self.assertEqual(Movies.objects.last().title, "dunkirk")
