from django.test import TestCase
from django.urls import reverse, resolve

from studios.models import Movies, Studio, Director
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


class TestMovieListView(TestCase, Mixin):
    def setUp(self):
        self.movie = self.create_movie()

    def test_page_serve_successful(self):
        url = reverse("movies:list")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_movie_list_object(self):
        view = resolve("/movie")
        self.assertEquals(view.func.view_class, views.MovieListView)

    def test_studio_filter_results(self):
        studio_id = self.movie.studio.id
        response = self.client.get(f"/movies/?genre=&studio={studio_id}")
        self.assertContains(response, self.movie)

    def test_genre_filter_results(self):
        genre = "comedy"
        response = self.client.get(f"/movies/?genre={genre}&studio=")
        self.assertNotContains(response, self.movie)


class TestMovieCreateView(TestCase, Mixin):
    def test_page_serve_successful(self):
        url = reverse("movies:create")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_movie_create_object(self):
        view = resolve("/movie/create")
        self.assertEquals(view.func.view_class, views.MovieCreateView)

    def test_presence_of_csrf(self):
        url = reverse("movies:create")
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
        url = reverse("movies:update", args=[self.movie.slug])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_movie_create_object(self):
        movie_slug = self.movie.slug
        view = resolve(f"/movie/{movie_slug}/update")
        self.assertEquals(view.func.view_class, views.MovieUpdateView)

    def test_presence_of_csrf(self):
        url = reverse("movies:update", args=[self.movie.slug])
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


class TestMovieDeleteView(TestCase, Mixin):
    def setUp(self):
        self.movie = self.create_movie()

    def test_page_serve_successful(self):
        url = reverse("movies:delete", args=[self.movie.slug])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_movie_delete_object(self):
        movie_slug = self.movie.slug
        view = resolve(f"/movie/{movie_slug}/delete")
        self.assertEquals(view.func.view_class, views.MovieDeleteView)


class TestDirectorDetailView(TestCase, Mixin):
    def setUp(self):
        self.movie = self.create_movie()

    def test_page_serve_successful(self):
        url = reverse("directors:detail", args=[self.movie.slug])
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_url_resolve_event_detail_object(self):
        view = resolve(f"/directors/{self.movie.slug}/detail")
        self.assertEquals(view.func.view_class, views.MovieDetailView)
